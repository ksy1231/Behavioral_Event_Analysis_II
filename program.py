import numpy as np
import pandas as pd


class Program:

    def toExcel(Pre_robot, Stim, Post_robot, Robot, Stim_all):
        name = {'Pre-robot': Pre_robot, 'Stim': Stim, 'Post-robot': Post_robot, 'Robot': Robot, 'Stim_all': Stim_all}
        data = pd.concat(name.values(), axis=1, keys=name.keys())
        df = data.fillna('')
        df.to_excel('Data.xlsx', sheet_name='Result')

    def sort(data, index, ascending):
        if ascending:
            return data.sort_values(by=[index], ascending=True)
        else:
            return data.sort_values(by=[index], ascending=False)

    def extract(data, index, chr):
        return data.loc[data[index].str.contains(chr)]

    def overlap(df):
        if df.empty:
            return df
        for _, row in df.iterrows():
            df_temp = df.copy()
            df_temp = df_temp[0].astype(float)
            df_temp.sort_index(inplace=True)
        for i in range(len(df_temp) - 1):
            row1, row2 = df_temp.iloc[i], df_temp.iloc[i + 1]
            if row2 - row1 < 0.04:
                df = df.drop(df.index[i + 1])
        return df

    def reshape(df, split):
        df_temp = df[0]
        row = int(split)  # 40
        col = int(len(df_temp) / int(split))  # 10
        df = pd.DataFrame(np.array(df_temp).reshape(col, row))
        data = df.T
        return data

    def drop_row(df):
        df_temp = df.copy()
        lit = []
        for i in range(len(df_temp) - 1):
            row1, row2 = df_temp.iloc[i], df_temp.iloc[i + 1]
            if row2 - row1 < 1:
                lit.append(i + 1)
        for i in lit:
            df = df.drop(i)
        df = df.reset_index(drop=True)
        return df

    def base(df, from_, to):
        preout = Program.enter_f1(df, from_, to)
        preout = Program.drop_row(preout)

        prepellet1 = Program.enter_pallet(df, from_, to)
        prepellet1 = Program.drop_row(prepellet1)

        prepellet2 = Program.pallet2(df, from_, to)
        prepellet2 = Program.drop_row(prepellet2)

        prein = Program.return_nest(df, from_, to)
        prein = Program.drop_row(prein)

        df = pd.DataFrame({"PreOut": preout, "Prepellet_1": prepellet1, "Prepellet_2": prepellet2, "PreIn": prein})
        return df

    def stim(df, from_, to, split):
        stim_out = Program.enter_f1(df, from_, to)
        stim_out = Program.drop_row(stim_out)

        if split != 0:
            stim_stim = Program.stimulation(df, from_, to, split)
            stim_stim = Program.drop_row(stim_stim)
        else:
            stim_stim = pd.Series()

        stimpellet1 = Program.enter_pallet(df, from_, to)
        stimpellet1 = Program.drop_row(stimpellet1)

        stimpellet2 = Program.pallet2(df, from_, to)
        stimpellet2 = Program.drop_row(stimpellet2)

        stim_in = Program.return_nest(df, from_, to)
        stim_in = Program.drop_row(stim_in)

        df = pd.DataFrame({"StimOut": stim_out, "Stim_light": stim_stim, "Stimpellet_1": stimpellet1,
             "Stimpellet_2": stimpellet2, "StimIn": stim_in})
        return df

    def post(df, from_, to):
        post_out = Program.enter_f1(df, from_, to)
        post_out = Program.drop_row(post_out)

        postpellet1 = Program.enter_pallet(df, from_, to)
        postpellet1 = Program.drop_row(postpellet1)

        postpellet2 = Program.pallet2(df, from_, to)
        postpellet2 = Program.drop_row(postpellet2)

        post_in = Program.return_nest(df, from_, to)
        post_in = Program.drop_row(post_in)

        df = pd.DataFrame(
            {"PostOut": post_out, "Postpellet_1": postpellet1, "Postpellet_2": postpellet2, "PostIn": post_in})
        return df

    def robot(df, from_, to):
        robot_out = Program.enter_f1(df, from_, to)
        robot_out = Program.drop_row(robot_out)

        robotpellet1 = Program.enter_pallet(df, from_, to)
        robotpellet1 = Program.drop_row(robotpellet1)

        robotpellet2 = Program.pallet2(df, from_, to)
        robotpellet2 = Program.drop_row(robotpellet2)

        robot_pallet = Program.pallet(df, from_, to)
        robot_pallet = Program.drop_row(robot_pallet)

        robot_in = Program.return_nest(df, from_, to)
        robot_in = Program.drop_row(robot_in)

        df = pd.DataFrame(
            {"RobotOut": robot_out, "RobotPellet_1": robotpellet1, "RobotPellet_2": robotpellet2,
             "Robot": robot_pallet, "RobotIn": robot_in})
        return df

    def stim_all(df):
        data_FFFF = Program.extract(df, 1, 'FFFF')
        sort_FFFF = Program.sort(data_FFFF, 0, True)
        df_overlap = Program.overlap(sort_FFFF)
        df_FFFF = df_overlap[0].reset_index(drop=True)
        df = pd.DataFrame({"Stim_all": df_FFFF})
        return df

    def enter_f1(df, x, y):
        data_out = Program.extract(df, 1, '3003')
        data = data_out.loc[(data_out[0] >= float(x)) & (data_out[0] <= float(y))]
        out = data[0].reset_index(drop=True)
        return out

    def enter_pallet(df, x, y):
        data_enter = Program.extract(df, 1, '3030')
        data = data_enter.loc[(data_enter[0] >= float(x)) & (data_enter[0] <= float(y))]
        enterpellet = data[0].reset_index(drop=True)
        return enterpellet

    def pallet2(df, x, y):
        data_pallet = Program.extract(df, 1, '3300')
        data = data_pallet.loc[(data_pallet[0] >= float(x)) & (data_pallet[0] <= float(y))]
        pellet_2 = data[0].reset_index(drop=True)
        return pellet_2

    def return_nest(df, x, y):
        data_in = Program.extract(df, 1, '30C0')
        data = data_in.loc[(data_in[0] >= float(x)) & (data_in[0] <= float(y))]
        returnnest = data[0].reset_index(drop=True)
        return returnnest

    def stimulation(df, x, y, split):
        data_stim = Program.extract(df, 1, 'FFFF')
        sort_data = Program.sort(data_stim, 0, True)
        data_overlap = Program.overlap(sort_data)
        data = data_overlap.loc[(data_overlap[0] >= float(x)) & (data_overlap[0] <= float(y))]
        data_reshape = Program.reshape(data, split)
        data_extract = data_reshape.loc[0]
        return data_extract

    def pallet(df, x, y):
        data_pallet = Program.extract(df, 1, '7')
        sort_data = Program.sort(data_pallet, 0, True)
        data = sort_data.loc[(sort_data[0] >= float(x)) & (sort_data[0] <= float(y))]
        act_pallet = data[0].reset_index(drop=True)
        return act_pallet
