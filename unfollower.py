"""
Unfollower

Find out who unfollowed you on Twitter
"""

import sqlalchemy
from datetime import datetime
import twitter
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Base, Follower
import config
import time


class Unfollower(object):
    def __init__(self):
        # Connect to Twitter API
        self.api = twitter.Api(
            consumer_key=config.CONSUMER_KEY,
            consumer_secret=config.CONSUMER_SECRET,
            access_token_key=config.ACCESS_TOKEN_KEY,
            access_token_secret=config.ACCESS_TOKEN_SECRET,
        )

        # Get a DB session
        engine = sqlalchemy.create_engine(config.DB_URI)
        Base.metadata.create_all(engine)

        self.session = scoped_session(sessionmaker(bind=engine))

    def update(self):

        previous_followers = self.session.query(Follower).filter_by(is_following=True).all()
        previous_followers_ids = [follower.twitter_id for follower in previous_followers]

        current_followers = self.api.GetFollowers()
        current_followers_ids = [follower.GetId() for follower in current_followers]
        #print "Found %d followers" % len(current_followers)

        # Add the new followers
        for follower in current_followers:
            if follower.GetId() not in previous_followers_ids:
                # New follower !
                print "[%s] Found a new follower : %s [%s] (#%d)" \
                    % (datetime.today().strftime('%d/%m %H:%M'), follower.GetName(), follower.GetScreenName(), follower.GetId())
                self.session.add(
                    Follower(
                        name=follower.GetName(),
                        screen_name=follower.GetScreenName(),
                        twitter_id=follower.GetId(),
                        is_following=True,
                        last_following=datetime.now(),
                    )
                )

        # Discover the unfollowers
        for old_follower in previous_followers:
            if old_follower.twitter_id not in current_followers_ids:
                # Unfollower !
                print "[%s] Found an unfollower : %s [%s] (#%d)" % \
                    (datetime.today().strftime('%d/%m %H:%M'), old_follower.name, old_follower.screen_name, old_follower.twitter_id)
                old_follower.is_following = False

        # Close the session
        self.session.commit()
        self.session.close()


if __name__ == '__main__':
    print "Launched unfoolower, waiting for new followers or unfollowers !"
    while True:
        Unfollower().update()
        time.sleep(60*60)
