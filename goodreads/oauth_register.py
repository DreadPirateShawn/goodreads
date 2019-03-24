import argparse
from .client import GoodreadsClient

def main(args):
    gc = GoodreadsClient(args.key, args.secret)
    gc.authenticate(None, None)
    summary = [
        "",
        "OAuth token: %s" % gc.session.access_token,
        "OAuth token secret: %s" % gc.session.access_token_secret,
        "",
        "Confirming authentication using these values...",
    ]
    print("\n".join(summary))
    gc.authenticate(gc.session.access_token, gc.session.access_token_secret)
    recap = [
        "",
        "Confirmed. Now you can use these to re-authenticate, e.g.",
        "  gc.authenticate(%s, %s)" % (gc.session.access_token, gc.session.access_token_secret),
        "",
    ]
    print("\n".join(recap))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', type=str, help='Goodreads API key', required=True)
    parser.add_argument('--secret', type=str, help='Goodreads API secret', required=True)
    args = parser.parse_args()
    main(args)
