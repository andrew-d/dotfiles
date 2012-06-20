Andrew's Dotfiles
=================

These are my dotfiles, along with an appropriate set of installation and updating scripts.  The organization is roughly as follows:

 - link/ contains files that will simply be symlinked to their respective files in ~ (e.g. link/bashrc is linked from ~/.bashrc)
 - copy/ contains files that are copied to the local/ directory, and then symlinked.  This is used for files with potentially sensitive information - for example, .gitconfig.  Note that the entire directory is recursively copied to the local/ folder, but only the files are symlinked.
 - pre_install/ contains scripts that will be run (in alphabetic sort order) before any symlinking or installing is done
 - post_install/ contains scripts that are run (in alphabetic sort order) after all files have been symlinked or copied (e.g. the script that prompts to set up git)


Subdirectories
--------------
In some of the subdirectories, there are subdirectories for architecture-specific stuff.  For example, the link/ directory has subdirectories Darwin/ and Linux/, which are used to store specific information for individual operating systems.  For example, bashrc will `source` a bashrc file from the appropriate subdirectory, if it exists.


Install Script
--------------
The install script will do the following, in the given order:

1. Run each file in pre_install/ in alphabetical order.
2. Link each file in link/ to the appropriate place in the home directory.  Backup anything that exists already.
3. Recursively copy the entirety of the copy/ directory to local/, and then symlink/backup anything in the same manner as link/.
4. Run each file in post_install/ in alphabetical order.

