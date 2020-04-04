from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

for year in range(2000, 2021):
    client.players_season_totals(
        season_end_year=year,
        output_type=OutputType.CSV,
        output_file_path=f"./SeasonData/{year}_totals.CSV",
    )
