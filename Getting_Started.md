# Overview #

SpicyMango allows the user to define search parameters (keywords) within the configuration files. Spicymango continuously searches/monitors publicly available internet resources, such as twitter, facebook, & irc channels using the defined keywords.  Keywords can also use specific operators/logic depending on what the target site/resource supports (such as AND/OR or API operators or irc commands).  The beta release supports the collection, aggregation and normalization of the unstructured data sources. There is a web console to help analysts use/consume the data it finds.

# Requirements #

  * Python >= v2.6 but < v3.0

# Getting Started #

## 1. Step One ##

Download the latest version of SpicyMango http://code.google.com/p/spicymango/source/checkout

## 2. Step Two ##

copy or rename the following files in spicymango directory:
  * config.sample -> config
  * keywords.sample -> keywords

## 3. Step Three ##

Enable the desired modules in the **config** file.
See Modules\_Options for Module options and details

## 4. Step Four ##

Edit the **keyword** file to specify the desired search terms for each module.
See [Keywords](Keywords.md) for more information

## 5. Step Five ##

Run **spicymango.py** (i.e. './spicymango.py' or 'python spicymango.py'

## 6. Step Six ##

Browse to
`http://127.0.0.1:8080/` to configure alert keywords and thresholds.

Default Credentials:
  * Username: **admin**
  * Password: **sm1234**