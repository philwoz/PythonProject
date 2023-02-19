from stats import pd


def get_fixt():
    fixtures = pd.read_csv(f'https://www.football-data.co.uk/fixtures.csv')
    fixt_stats = pd.DataFrame(columns=["Date", "Div", "HomeTeam", "AwayTeam"])
    for i, row in fixtures.iterrows():
        league = row["Div"]
        if league != "EC":
            new_row = [row["Date"], row["Div"], row['HomeTeam'], row['AwayTeam']]
            fixt_stats.loc[i] = new_row
    return fixt_stats.to_dict('index')
