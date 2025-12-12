from app.compute import compute_stats, prime_factors

def test_compute_stats_basic():
    res = compute_stats([1, 2, 3, 4])
    assert res["count"] == 4.0
    assert round(res["mean"], 2) == 2.5

def test_prime_factors_basic():
    assert prime_factors(12) == [2, 2, 3]
