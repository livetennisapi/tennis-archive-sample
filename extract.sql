COPY (
  SELECT
    tournament        AS tourney_name,
    level             AS tourney_level,
    surface,
    draw_size,
    to_char(event_date,'YYYY-MM-DD') AS tourney_date,
    round,
    best_of,
    minutes,
    winner_name,
    winner_hand,
    winner_ht,
    upper(winner_country)   AS winner_ioc,
    round(winner_age::numeric,1) AS winner_age,
    winner_rank,
    winner_seed,
    winner_entry,
    loser_name,
    loser_hand,
    loser_ht,
    upper(loser_country)    AS loser_ioc,
    round(loser_age::numeric,1)  AS loser_age,
    loser_rank,
    loser_seed,
    loser_entry,
    score,
    outcome
  FROM archive_matches
  WHERE tour='atp'
    AND level IN ('G','M','A','F')
    AND extract(year from event_date)=2015
  ORDER BY event_date, tournament, id
) TO STDOUT WITH (FORMAT csv, HEADER true);
