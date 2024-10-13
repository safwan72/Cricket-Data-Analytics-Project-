import pandas as pd
import json


# match_summary
with open(
    r"C:\Users\safwa\OneDrive\Desktop\DA\project\t20_json_files\t20_wc_match_results.json"
) as f:
    data=json.load(f)

df_matchSum = pd.DataFrame(data[0]["matchSummary"])

# Renaming Column value
df_matchSum.rename({'scorecard':'match_id'},axis=1,inplace=True)
# print(df_matchSum)


df_matchSum_dict={}

for index,row in df_matchSum.iterrows():
    key1 = row["team1"] + " Vs " + row["team2"]
    key2 = row["team2"] + " Vs " + row["team1"]

    df_matchSum_dict[key1]=row['match_id']
    df_matchSum_dict[key2]=row['match_id']

# print(df_matchSum_dict)
# Exporting
# df_matchSum.to_csv("t20_csv_files/t20_wc_match_summary.csv", index=False)


# batting_summary

with open(
    r"C:\Users\safwa\OneDrive\Desktop\DA\project\t20_json_files\t20_wc_batting_summary.json"
) as f1:
    all_rec=[]
    data=json.load(f1)
    for rec in data:
        all_rec.extend(rec["battingSummary"])

# print(all_rec)
df_battingSum = pd.DataFrame(all_rec)


# Changing One column value depending on other
df_battingSum["batsman_status"] = df_battingSum['dismissal'].apply(lambda x:'out' if len(x)>1 else 'not out')


# dropping column from dataframe, inplace important otherwise wont replace main data
df_battingSum.drop(columns=["dismissal"],inplace=True)


# replacing characters from a column value in dataframe
df_battingSum["batsmanName"] = df_battingSum["batsmanName"].apply(
    lambda x: x.replace("†", "")
)


df_battingSum["match_id"] = df_battingSum["match"].map(df_matchSum_dict)
# print(df_battingSum.head(40))


# Exporting
# df_battingSum.to_csv("t20_csv_files/t20_wc_batting_summary.csv",index=False)


# bowling_summary

with open(
    r"C:\Users\safwa\OneDrive\Desktop\DA\project\t20_json_files\t20_wc_bowling_summary.json"
) as f1:
    all_rec = []
    data = json.load(f1)
    for rec in data:
        all_rec.extend(rec["bowlingSummary"])

df_bowlingSum = pd.DataFrame(all_rec)

df_bowlingSum["match_id"] = df_bowlingSum["match"].map(df_matchSum_dict)
# print(df_bowlingSum.head(40))
# Exporting
# df_bowlingSum.to_csv("t20_csv_files/t20_wc_bowling_summary.csv",index=False)


# player_summary

with open(
    r"C:\Users\safwa\OneDrive\Desktop\DA\project\t20_json_files\t20_wc_player_info.json"
) as f4:
    all_rec = []
    data = json.load(f4)
df_playerSum = pd.DataFrame(data)

#print(df_playerSum)


# Exporting
#df_playerSum.to_csv("t20_csv_files/t20_wc_player_summary.csv", index=False)
