## Command Mode

### KEYBINDS ARE CASE SENSITIVE!

 ``!`` - Forces an Action. Overrides warnings. It is to be applied as a suffix. (Such as ``:q!``)

``/[pattern]`` - Searches.It is to be applied as a suffix. (Such as ``/Closed`)
``esc`` - Enters Command Mode

``a`` - Append Mode (inserts to the right of the cursor

``i`` - Insert Mode (Overwrites the character at the cursor)

``O`` - Opens line above current line.

``o`` - Opens line below the current line.

``ZZ`` - Saves & Exits.

``x`` - deletes one character

``dd`` - deletes 1 line.

``u`` - Undoes last change.

``LEFT RIGHT`` - Arrow Keys allow you to move within your lines, can only be used within command mode, otherwise character input is messed up.

``:`` - Instructs Vim to accept multiple characters within command mode, to allow the input of actual commands. (Such as ``:save ...``)

``:save [name | name.ext]`` - Saves Vim File with custom name, and or name with a custom file extension. (Such as ``:save systemAudit.txt`` or ``:save who_am_i``)

``:w`` - Saves Changes.

``:q`` - Quits.

``:wq`` - Saves and Quits.

``:w [file.ext]`` - Saves Changes, and changes name.

``$ vi`` - Opens Vim.

``vi [file.ext]`` - Opens existing Vim file.






