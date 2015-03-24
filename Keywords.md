# Overview #

These keywords are defined in the **keywords** file.

**Note:** They are not to be confused with the keyword terms you define in the Web [GUI Options](GUI_Options.md). Basically, the difference is that the modules that query an API must supply a search term to receive data. So, these keyword terms should be very broad. More detailed analysis can be achieved with the keyword terms specified in the SpicyMango GUI on the data returned by these modules. Clear as mud?

---



### Format ###

The format for a module keyword term is as follows:

` ['mod_name','search_term'] `

  * Some modules, like mod\_irc, can take regular expressions.
  * Some modules, like mod\_twitter, can use operators for the API itself.
  * The facebook module can only use single string search terms with no spaces.

---



### Initialization ###

For the mod\_twitter and mod\_facebook modules, a new thread is started for each search term. That is because you can only make one query per GET request to the API. This means that the more search terms you define per these modules, the more requests you will make to the API's. This needs to be considered because both API's have limits to how many queries can be executed within a certain amount of time. You will need to adjust the module intervals in the **config** file to keep from getting these errors.