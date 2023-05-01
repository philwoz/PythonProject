from stats import pd
import datetime


def get_fixt():
    fixtures = pd.read_csv(f'https://www.football-data.co.uk/fixtures.csv')
    fixt_stats = pd.DataFrame(columns=["Date", "Div", "HomeTeam", "AwayTeam"])
    today = str(datetime.date.today())
    today1 = f"{today[-2:]}/{today[-5:-3]}/{today[0:4]}"
    for i, row in fixtures.iterrows():
        league = row["Div"]
        if league != "EC":
            new_row = [row["Date"], row["Div"], row['HomeTeam'], row['AwayTeam']]
            fixt_stats.loc[i] = new_row
    fixt_stats = fixt_stats[fixt_stats.Date == today1]
    return fixt_stats.to_dict('index')
