# Overview #

Below is a list of available modules for SpicyMango. The configurable options for each module are available in the **config** file.

---


### MOD\_IRC ###
**This spawns an ircbot that connects to a specific IRC server and joins the configured IRC channels. It records any messages sent in the channel based on a matched string or regular expression defined in the [Keywords](Keywords.md) file.**

` MOD_IRC=[ON | OFF] `

This enables or disables the module.

` MOD_IRC_SERVER=[ "irc.server.com" ] `

This tells the IRC module which IRC server to connect to.

` MOD_IRC_CHANNELS=[ "channel[1]"[, "channel[2]..."] ] `

This defines the list of IRC channels to connect to on the IRC Server.

` MOD_IRC_USER=[ "userhandle" ] `

This is the name the ircbot will use when it joins the channels.

---


### MOD\_TWITTER ###
**This Queries the Twitter API for tweets based on the search criteria configured in the [Keywords](Keywords.md) file.**

` MOD_TWITTER=[ON | OFF] `

This enables or disables the module.

` MOD_TWITTER_COUNT=[ Number ] `

This specifies how many records to retrieve per request. The default is **5**. Keep this low if you have multiple search terms configured in the [Keywords](Keywords.md) file.

` MOD_TWITTER_INTERVAL=[ Number ] `

This is the time, **in seconds**, that each instance of the module will query the Twitter API for information. Twitter will reject too many requests, so if you define multiple search terms, keep this number higher. The default is **15** seconds.

**Note:** A new instance of the module is spawned for each search term defined in the [Keywords](Keywords.md) file for this module.

---


### MOD\_FACEBOOK ###
This uses Facebook's Graph API to query for Facebook posts that match the search terms defined in the [Keywords](Keywords.md) file.

` MOD_FACEBOOK=[ ON | OFF ] `

This enables or disables the module.

` MOD_FACEBOOK_INTERVAL=[ Number ] `

This is the time, **in seconds**, that each instance of the module will query the Facebook API for information.

**Note:** A new instance of the module is spawned for each search term defined in the [Keywords](Keywords.md) file for this module.

---


### MOD\_RSS ###
**The RSS module reads in a list of RSS feeds and a regular expression and then searches for relevant posts. Supports RSS and Atom feed types.**

` MOD_RSS=[ ON | OFF ] `

This enables or disables the module.

` MOD_RSS_INTERVAL=[ Number ] `

This is the time, **in seconds**, that each RSS feed will be collected.


---


### MOD\_GMAIL ###
**This module uses Gmail's IMAP support to download messages based on the label they are under. For example, the messages in the inbox have the label "Inbox." Messages that are starred are given the label "[Gmail](Gmail.md)/Starred". Ideally the gmail account should be setup to filter relevant information into labels that you can search.**

` MOD_GMAIL=[ ON | OFF ] `

This enables or disables the module.

` MOD_GMAIL_INTERVAL=[ Number ] `

This is the time, **in seconds**, that each RSS feed will be collected.

{{{ MOD\_GMAIL\_EMAIL=[The gmail email address ](.md)

The full email address of the account being accessed

{{{ MOD\_GMAIL\_PASSWORD=[Password ](.md)

The password of the gmail account being used. NOTE: This is not a secure way of handling the passwords at this point. Plan accordingly.