# discord-bot2.0
(all code is in py folder :)

i actually understand code now so this will be interesting.
this README will serve as a daily log for me and to see my progress. i will also be doing daily commits if i work on the files at all. if there is little to no change i will not be commiting. i will be logging what ive learned today as well as other things

**3/29/22** 
repo is set up and dpy is installed just reading the docs to learn how to acutally use discord.py. hoping its easier then discord.js took 3 days to get discord.py to actually work so thats nice. everyone was relatively helpful and helped me solve a specific issue. only need to figure out how to hide the token and i can make the repo open. ok its whatever ill just make it priv.

**4/1/22:** 
decided to do both py and js. placed them in seperate folders. and token.json should be easier to understand. i figured out dotenv so the repo is now open. decided to fuck js its too hard lmao. i think py will be easier i just gotta get the hang of it. 

**4.1.22 commit message:** just commiting to show progress this commit is meaningless bc nothing besides figuring out dotenv worked lol. (brads fucking dumb)


**4.3.22:** 
i sorta figured out intents and imma make some commands today
decided to remove all non-working commands and added some quality-of-life changes to my extensions in vscode. i will list them in extenstions.txt. still cant figure out why my commands arent working . ill figure it out later. no commit today for no changes. if i can figure out a way to fix it there will be a commit today. still no luck on figureing out how to fix this bug. just gonna commit it


**4.3.22 commit message:** removed non-working lines (events, commands, ect), added extensions.txt and load.txt, added to .gitignore, added extra comments. other commands still not working. bug fix in progress


**4.4.22:**
ok so i think i fixed the command thing. i posted about it on the discussions in the dpy repo and the person who made dpy replied to add this little thing to the end of one of my commands and im waiting to see if it works. and it works. for some reason using on_message command overrides everything and forbids commands from running. not sure why but its listed in the docs right here:(https://discordpy.readthedocs.io/en/stable/faq.html#why-does-on-message-make-my-commands-stop-working). good to know that its solved and i can finally get to work. 

**4.4.22 commit message:** 
added "list" command, added embed to 'list' command, created (not tested yet) onjoin message, created an "unknown command" event, created help command, fixed commands not running, added brief description to commands. 
**4.4.22 issues:**
dm commands not working and i am yet to figure out how to use the help command.


**4.5.22**
fixed help command issues. just doing embeds for it now. adding a purge command(in progress), added meme commands jsut for trolls their kind of meaningless and i intend to remove them. nothing much happened today so hopefully tomorrow is more successful


**4.5.22 commit message:**
Removed DM_LIST command, removed custom help command for maintenance (placed in storage.txt), added PURGE command(doesnt currently work, placed in storage; not in bot.py file),  added meme commands, re-added COMMAND NOT FOUND message, added commands to LIST command(not available rn), added to gitignore


**4.6.22:**
decided to add admin commands to make the bot more useful. adding "admin" arg to list as well so admins can see their commands but im going to make it dm them the list. planning on adding a self-role system once i figure out how to do that. on_join and on_member_join still doesnt work and needs to be fixed. otherwise today was sucessful. seriously thinking about new commands to add beacuse im running out of ideas. only other solution would be to do voice commands, those should entertain me for a while. 

**4.6.22 commit message:**
added admin commands(kick, ban, unban), added ADMINCMD command; dms user list of admin commands, removed LIST command, learned some new stuff, added a variable to make coloring embeds easier


**4.6.22**
i have nothing to log so just the commit message 


**4.6.22 commit message:**
added fun commands(dice roll, coin flip), made README look nicer, added CREATOR and OWNER commands, added a new file(issues checklist.txt), 
