from stats import pd


def btts_table(cntry, div, year, sort="Total %", num_games=None):
    df = pd.read_csv(f'https://www.football-data.co.uk/mmz4281/{year - 1}{year}/{cntry}{div}.csv')
    def conditions(s):
        if (s['FTHG'] > 0) and (s['FTAG'] > 0):
            return 1
        else:
            return 0

    table = []
    teams = df.HomeTeam.unique()
    df['BTTS'] = df.apply(conditions, axis=1)
    if num_games == None:
        num_games = len(teams) - 1

    for team in teams:
        home_filt = df[df['HomeTeam'] == team].tail(num_games)
        away_filt = df[df['AwayTeam'] == team].tail(num_games)
        played = len(home_filt) + len(away_filt)
        btts_hm = round(home_filt['BTTS'].mean(), 2) * 100
        btts_aw = round(away_filt['BTTS'].mean(), 2) * 100
        total = round(((home_filt['BTTS'].sum() + away_filt['BTTS'].sum()) / played), 2) * 100

        table.append([team, played, round(btts_hm), round(btts_aw), round(total)])

    league = pd.DataFrame(table, columns=["Team", "Played", "Home %", "Away %", "Total %"])
    return league.sort_values(by=[sort], ascending=False).reset_index(drop=True).to_dict('index')


def league_table(cntry, div, year, full=False, num_games=None):
    df = pd.read_csv(f'https://www.football-data.co.uk/mmz4281/{year-1}{year}/{cntry}{div}.csv')
    table = []
    teams = df.HomeTeam.unique()
    if num_games == None:
        num_games = len(teams) - 1

    for team in teams:
        points = 0
        home_filt = df[df['HomeTeam'] == team].tail(num_games)
        away_filt = df[df['AwayTeam'] == team].tail(num_games)

        played = len(home_filt) + len(away_filt)
        home_wins = len(home_filt[home_filt['FTR'] == 'H'])
        home_draws = len(home_filt[home_filt['FTR'] == 'D'])
        home_loss = len(home_filt[home_filt['FTR'] == 'A'])
        home_for = home_filt.FTHG.sum()
        home_ang = home_filt.FTAG.sum()
        away_wins = len(away_filt[away_filt['FTR'] == 'A'])
        away_draws = len(away_filt[away_filt['FTR'] == 'D'])
        away_loss = len(away_filt[away_filt['FTR'] == 'H'])
        away_for = away_filt.FTAG.sum()
        away_ang = away_filt.FTHG.sum()
        total_win = home_wins + away_wins
        total_draw = home_draws + away_draws
        total_loss = home_loss + away_loss
        total_for = home_for + away_for
        total_ang = home_ang + away_ang
        gl_dif = total_for - total_ang
        home_points = (home_wins * 3) + home_draws
        away_points = (away_wins * 3) + away_draws
        points = home_points + away_points
        if full == False:
            table.append([team, played, total_win, total_draw, total_loss, gl_dif, points])
        elif full == "All":
            table.append([team, len(home_filt), home_wins, home_draws, home_loss, home_for, home_ang,
                          home_points, len(away_filt), away_wins, away_draws, away_loss, away_for, away_ang,
                          away_points, total_for, total_ang, gl_dif, points])
        elif full == "Home":
            table.append([team, len(home_filt), home_wins, home_draws, home_loss, home_for, home_ang,
                          home_points])
        elif full == "Away":
            table.append([team, len(away_filt), away_wins, away_draws, away_loss, away_for, away_ang,
                          away_points])

    if full == False:
        league = pd.DataFrame(table, columns=["Team", "Played", "W", "D", "L", "GD", "PTS"])
        return league.sort_values(by=["PTS", "GD"], ascending=False).reset_index(drop=True).to_dict('index')
    elif full == "All":
        league = pd.DataFrame(table,
                              columns=["Team", "Home", "HW", "HD", "HL", "HGF", "HGA", "H-PTS", "Away", "AW", "AD",
                                       "AL",
                                       "AGF", "AGA", "A-PTS", "GF", "GA", "GD", "PTS"])
        return league.sort_values(by=["PTS", "GD", "GF"], ascending=False).reset_index(drop=True).to_dict('index')
    elif full == "Home":
        league = pd.DataFrame(table, columns=["Team", "Home", "HW", "HD", "HL", "HGF", "HGA", "H-PTS"])
        return league.sort_values(by=["H-PTS", "HW", "HD", "HGF"], ascending=False).reset_index(drop=True).to_dict('index')
    elif full == "Away":
        league = pd.DataFrame(table, columns=["Team", "Away", "AW", "AD", "AL", "AGF", "AGA", "A-PTS"])
        return league.sort_values(by=["A-PTS", "AW", "AD", "AGF"], ascending=False).reset_index(drop=True).to_dict('index')
