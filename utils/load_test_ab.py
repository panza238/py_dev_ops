"""
Simple script to demonstrate how the ab CLI tool works
"""
import subprocess
import click


@click.command()
@click.option('-n', type=int, default=15, help="number of total requests for the test")
@click.option('-c', type=int, default=3, help="number concurrent requests for the test")
@click.argument('url', required=True, type=str)
def run_load_test_ab(n, c, url):
    """run a simple load test by using ab CLI tool, through the subprocess module.
    :argument url: url to load test\n
    example: run_load_test_ab -n 15 -c 3 http://google.com will run a simple load test
    with 15 total requests, 3 requests at a time."""
    subprocess.run(["ab", "-n", str(n), "-c", str(c), url])


if __name__ == "__main__":
    run_load_test_ab()
