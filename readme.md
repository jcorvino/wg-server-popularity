# Welcome to wg-server-popularity
This is a project to track the number of active players across all Wargaming games.
The goal is to create realtime displays and graphs of players over time. 
Here's an example of such a graph from Steam:
![Steam Example Graph](https://raw.githubusercontent.com/jcorvino/wg-server-popularity/master/images/steam-example.png "Steam Example Graph")


### How to use
1. Install Python 3.8
2. Install dependencies `pip install -r requirements.txt`
3. Obtain a [Wargaming API key](https://developers.wargaming.net/applications/)
4. Create an environment variable called `WG_API_SECRET` and set it to your WG API key.
5. Run `python app.py`
