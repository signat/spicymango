# Overview #

The feeds file is a list of RSS feeds used by the mod\_rss module. It consists of a feed URL, the regular expression to search for, and whether the request to collect the feed should be anonymized through Tor.

---



### Format ###

The format for a module keyword term is as follows:

` ['feed url','regex search term'], 'ON or OFF']`


---


### Tor Support ###

In order for requests to be anonymized, a running instance of Tor must be accessible. This is done simply by:
  1. Installing Tor
  1. Modifying the TORRC file to enable the control port on 9051
  1. Starting Tor

The corresponding configuration items should match up with your setup:

  * TOR\_HOST="localhost"
  * TOR\_PORT=9050
  * TOR\_CTL\_PORT=9051
  * TOR\_PASS=""

NOTE: This is not a fully anonymized setup. The purpose is to make it difficult for the remote host to attribute a request to a specific source but it should not yet be relied upon for complete anonymity.