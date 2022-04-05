# discord-bot2.0
i actually understand code now so this will be interesting
this README will serve as a daily log for me and to see my progress. i will also be doing daily commits if i work on the files at all. if there is little to no change i will not be commiting. i will be logging what ive learned today as well as other things

**3/29/22** 
repo is set up and dpy is installed just reading the docs to learn how to acutally use discord.py. hoping its easier then discord.js took 3 days to get discord.py to actually work so thats nice. everyone was relatively helpful and helped me solve a specific issue. only need to figure out how to hide the token and i can make the repo open. ok its whatever ill just make it priv.

**4/1/22:** 
decided to do both py and js. placed them in seperate folders. and token.json should be easier to understand. i figured out dotenv so the repo is now open. decided to fuck js its too hard lmao. i think py will be easier i just gotta get the hang of it. 

**4.1.22** 
commit message: just commiting to show progress this commit is meaningless bc nothing besides figuring out dotenv worked lol. (brads fucking dumb)


**4.3.22:** 
i sorta figured out intents and imma make some commands today
decided to remove all non-working commands and added some quality-of-life changes to my extensions in vscode. i will list them in extenstions.txt. still cant figure out why my commands arent working . ill figure it out later. no commit today for no changes. if i can figure out a way to fix it there will be a commit today. still no luck on figureing out how to fix this bug. just gonna commit it


**4.3.22** commit message: removed non-working lines (events, commands, ect), added extensions.txt and load.txt, added to .gitignore, added extra comments. other commands still not working. bug fix in progress


**4.4.22:**
ok so i think i fixed the command thing. i posted about it on the discussions in the dpy repo and the person who made dpy replied to add this little thing to the end of one of my commands and im waiting to see if it works. and it works. for some reason using on_message command overrides everything and forbids commands from running. not sure why but its listed in the docs right here:(https://discordpy.readthedocs.io/en/stable/faq.html#why-does-on-message-make-my-commands-stop-working). good to know that its solved and i can finally get to work. 

**4.4.22 commit message:** 
added "list" command, added embed to 'list' command, created (not tested yet) onjoin message, created an "unknown command" event, created help command, fixed commands not running, added brief description to commands. 
**4.4.22 issues:**
dm commands not working and i am yet to figure out how to use the help command.
