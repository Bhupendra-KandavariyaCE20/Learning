# Git Tutorial for Ubuntu

A practical, beginner-friendly guide to using Git on Ubuntu Linux.
Commands are intended for the Ubuntu terminal, including Ubuntu running
in WSL on Windows.

## 1. What is Git?

Git is a **version control system**. It records changes to files so you
can review your work, restore earlier versions, and collaborate with
other developers.

Important terms:

-   **Repository (repo):** A project tracked by Git.
-   **Working directory:** The files you are currently editing.
-   **Staging area:** The changes selected for the next commit.
-   **Commit:** A saved snapshot of staged changes.
-   **Branch:** An independent line of development.
-   **Remote:** A copy of the repository hosted elsewhere, commonly on
    GitHub.
-   **Clone:** Downloading a repository and its history.
-   **Push / pull:** Sending commits to a remote / bringing remote
    changes into your local repository.

### The basic workflow

``` text
Edit files
   ↓
git add        (choose changes)
   ↓
git commit     (save a snapshot locally)
   ↓
git push       (send commits to a remote, such as GitHub)
```

`git add` does not upload files, and `git commit` does not upload them
either. A push is needed to send commits to a remote.

## 2. Install Git on Ubuntu

Update package information and install Git:

``` bash
sudo apt update
sudo apt install git
```

Check the installation:

``` bash
git --version
```

If you are using Ubuntu in WSL, run these commands inside the Ubuntu
terminal.

## 3. Configure your identity

Set the name and email that Git will record in your commits:

``` bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Check your configuration:

``` bash
git config --global --list
```

To inspect where a particular setting comes from:

``` bash
git config --show-origin --get user.name
```

Use an email address appropriate for your Git hosting account. Git
configuration does not itself sign you in to GitHub.

## 4. Create your first repository

Create a practice project:

``` bash
mkdir git-practice
cd git-practice
git init
```

Git creates a hidden `.git` directory containing repository history and
metadata. Do not manually edit or delete it.

Check the status:

``` bash
git status
```

Create a file:

``` bash
echo "# Git Practice" > README.md
```

Check what changed:

``` bash
git status
git diff
```

A new, untracked file will not appear in `git diff` by default. Stage it
first to prepare it for a commit.

## 5. Stage and commit changes

Stage a specific file:

``` bash
git add README.md
```

Stage all changes under the current directory:

``` bash
git add .
```

Review the staged changes:

``` bash
git status
git diff --staged
```

Commit them:

``` bash
git commit -m "Add README"
```

A good commit message briefly describes the change, for example:

``` text
Add input validation
Fix login error handling
Document installation steps
```

Check recent commits:

``` bash
git log
git log --oneline
git log --oneline --graph --decorate --all
```

### Remember the three main states

-   **Modified:** A tracked file has changed in the working directory.
-   **Staged:** A change is selected for the next commit.
-   **Committed:** The staged snapshot has been saved in local history.

## 6. Understand `git status` and `git diff`

These commands answer different questions:

``` bash
git status           # Which files have changed, and what state are they in?
git diff             # Unstaged changes to tracked files
git diff --staged    # Changes staged for the next commit
git diff HEAD        # Changes in the working tree and index compared with HEAD
```

Run `git status` frequently. It is one of the safest ways to understand
what Git is about to do.

## 7. Add a `.gitignore` file

`.gitignore` tells Git which **untracked** files it should generally
ignore. It does not automatically stop tracking files that are already
committed.

Create one:

``` bash
cat > .gitignore <<'EOF'
# Python
__pycache__/
*.py[cod]
.venv/
venv/

# Secrets and local configuration
.env

# Editor / OS files
.vscode/
.DS_Store
EOF
```

Review it before committing:

``` bash
cat .gitignore
git status
git add .gitignore
git commit -m "Add Git ignore rules"
```

**Important:** Never commit passwords, API keys, private keys, access
tokens, or other secrets. If a secret was committed, removing it in a
later commit does not erase it from history; revoke or rotate it and
follow an appropriate history-cleanup process.

If a file is already tracked and should no longer be tracked, you can
remove it from Git's index while keeping it locally:

``` bash
git rm --cached path/to/file
```

Then commit the change. Make sure the file is covered by `.gitignore` if
appropriate.

## 8. Work with branches

Branches let you develop a feature or fix without changing the main line
of development directly.

List branches:

``` bash
git branch
git branch -a
```

Create and switch to a branch:

``` bash
git switch -c feature/add-login
```

Make changes, then stage and commit them:

``` bash
git add .
git commit -m "Add login feature"
```

Switch back to the main branch:

``` bash
git switch main
```

The default branch may be named `master` in an older repository. Use the
branch name shown by `git branch` if it is not `main`.

Switch to an existing branch:

``` bash
git switch feature/add-login
```

Delete a branch that has already been merged:

``` bash
git branch -d feature/add-login
```

The `-D` option forces deletion of an unmerged branch. Use it only when
you are sure you no longer need its commits.

## 9. Merge a branch

To merge a feature branch into `main`:

``` bash
git switch main
git merge feature/add-login
```

If Git can merge the changes automatically, it will do so. If both
branches changed the same part of a file, Git may report a **merge
conflict**.

### Resolve a merge conflict

1.  Run `git status` to see the conflicted files.

2.  Open each conflicted file in an editor.

3.  Find conflict markers such as:

    ``` text
    <<<<<<< HEAD
    content from the current branch
    =======
    content from the branch being merged
    >>>>>>> feature/add-login
    ```

4.  Edit the file so it contains the final intended content, and remove
    the conflict markers.

5.  Stage the resolved file and finish the merge:

    ``` bash
    git add path/to/conflicted-file
    git status
    git commit
    ```

Git may open an editor for the merge commit message. Follow the
instructions shown in the terminal. If you are unsure what is happening,
do not blindly commit; inspect `git status` first.

## 10. Connect a local repository to GitHub

First, create an empty repository on GitHub. If you already have a local
project, avoid initializing the GitHub repository with a README or other
files unless you know how you will reconcile the histories.

Add the remote URL (replace the example with your repository URL):

``` bash
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git remote -v
```

If your local branch is named `main`, push it and set its upstream:

``` bash
git push -u origin main
```

If your branch has a different name, use that name instead.

### Authentication

GitHub does not accept your account password for ordinary Git HTTPS
operations. Depending on your setup, authenticate using a supported
credential manager, a personal access token when prompted by an
appropriate tool, or SSH keys.

For SSH, after creating and adding an SSH public key to your GitHub
account, the remote usually looks like:

``` bash
git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
```

Test SSH authentication:

``` bash
ssh -T git@github.com
```

Only add your **public** key (often ending in `.pub`) to GitHub. Never
share or upload your private key.

## 11. Clone an existing repository

To download an existing repository:

``` bash
git clone https://github.com/OWNER/REPOSITORY.git
cd REPOSITORY
```

Inspect the remote and branch:

``` bash
git remote -v
git branch
git status
```

To clone over SSH, use the SSH URL provided by the hosting service.

## 12. Fetch, pull, and push

-   `git fetch` downloads remote updates but does not merge them into
    your current branch.
-   `git pull` fetches updates and integrates them into your current
    branch (the exact integration behavior depends on configuration).
-   `git push` sends your local commits to a remote branch.

Typical workflow:

``` bash
git status
git pull
# Edit files
git add .
git commit -m "Describe your change"
git push
```

If you are working with others, commit or safely store your local
changes before pulling. If Git reports conflicts, resolve them before
continuing.

To fetch remote information without integrating it:

``` bash
git fetch origin
git log --oneline --decorate --all
```

## 13. Undo changes safely

Git has several different kinds of undo. Choose based on whether the
change is unstaged, staged, or already committed.

### Discard unstaged edits to a tracked file

``` bash
git restore path/to/file
```

This discards the file's unstaged edits. They may be difficult or
impossible to recover, so inspect the file first if you need its
contents.

### Unstage a file but keep its edits

``` bash
git restore --staged path/to/file
```

This removes the file from the staging area while keeping the
working-directory edits.

### Undo the latest commit without rewriting history

``` bash
git revert HEAD
```

This creates a new commit that reverses the changes from the latest
commit. It is often the safer choice for commits that have already been
shared.

### Amend the most recent commit

``` bash
git add path/to/file
git commit --amend
```

Amending replaces the latest commit with a new one. Avoid amending
commits that others already depend on unless you understand the
consequences of rewriting history.

### Reset a local branch

``` bash
git reset --soft HEAD~1
```

This moves the current branch back one commit while keeping the changes
staged. Other modes behave differently:

-   `--mixed` (the default) keeps changes in the working directory but
    unstages them.
-   `--hard` resets the index and working files and can permanently
    discard work.

Use `git reset --hard` only when you are certain that you do not need
the affected changes. Do not run destructive commands just to clear a
warning.

## 14. Useful inspection commands

``` bash
git status
git log --oneline --graph --decorate --all
git show
git show COMMIT_ID
git diff
git diff --staged
git branch -vv
git remote -v
git ls-files
```

To see which files are tracked, use `git ls-files`. To check whether a
path is ignored and why:

``` bash
git check-ignore -v path/to/file
```

## 15. Rename and delete tracked files

Git can detect many renames automatically, but these commands make your
intent clear:

``` bash
git mv old-name.txt new-name.txt
git rm file-to-delete.txt
git status
git commit -m "Rename file and remove obsolete file"
```

`git rm` removes the file from the working directory and stages the
deletion. To stop tracking a file while keeping the local copy, use
`git rm --cached filename` instead.

## 16. Stash unfinished work

Stashing temporarily stores working changes so you can switch tasks.

``` bash
git stash push -m "Work in progress"
git stash list
git stash show -p
git stash pop
```

`git stash pop` reapplies the stash and removes it from the stash list
if successful. If you want to reapply changes while keeping the stash
entry, use:

``` bash
git stash apply
```

Stash behavior can depend on whether changes are tracked, untracked, or
ignored. To include untracked files in a stash:

``` bash
git stash push -u -m "Include untracked files"
```

## 17. Tags

Tags label important points in history, commonly releases:

``` bash
git tag
git tag -a v1.0.0 -m "Release version 1.0.0"
git show v1.0.0
git push origin v1.0.0
```

To push all local tags:

``` bash
git push origin --tags
```

## 18. A complete practice exercise

Run this sequence in a new practice folder:

``` bash
mkdir git-exercise
cd git-exercise
git init

echo "# My Project" > README.md
git status
git add README.md
git diff --staged
git commit -m "Create project README"

echo "Git practice notes" >> README.md
git diff
git add README.md
git commit -m "Add practice notes"

git log --oneline
git switch -c feature/add-notes
echo "A new section" > notes.txt
git add notes.txt
git commit -m "Add notes file"

git switch main
git merge feature/add-notes
git log --oneline --graph --decorate
git status
```

If your initial branch is not called `main`, replace `main` with the
actual branch name shown by `git branch`.

## 19. Common problems

### `git: command not found`

Install Git:

``` bash
sudo apt update
sudo apt install git
```

### `Author identity unknown`

Configure your name and email as shown in Section 3.

### `fatal: not a git repository`

Move into the project folder that contains the repository, or initialize
a repository with `git init` if that is your intention.

### `src refspec main does not match any`

Common causes include having no commits yet or trying to push a branch
that does not exist. Check:

``` bash
git status
git branch
git log --oneline
```

Make an initial commit and push the actual branch name.

### Push rejected because the remote contains work you do not have

Fetch and inspect the remote history before integrating it:

``` bash
git fetch origin
git log --oneline --graph --decorate --all
```

Then choose an appropriate merge or rebase workflow. Avoid force-pushing
as a first fix, especially on a shared branch.

### Accidentally staged a file

``` bash
git restore --staged path/to/file
```

This unstages the file but preserves its working-directory changes.

## 20. Quick reference

  Goal                              Command
  --------------------------------- -------------------------------
  Initialize repository             `git init`
  Check status                      `git status`
  Stage a file                      `git add file`
  Stage current-directory changes   `git add .`
  Commit staged changes             `git commit -m "message"`
  View history                      `git log --oneline`
  View unstaged changes             `git diff`
  View staged changes               `git diff --staged`
  Create and switch branch          `git switch -c branch-name`
  Switch branch                     `git switch branch-name`
  Merge branch                      `git merge branch-name`
  Clone repository                  `git clone URL`
  Download remote updates           `git fetch`
  Integrate remote updates          `git pull`
  Upload commits                    `git push`
  Add remote                        `git remote add origin URL`
  Unstage a file                    `git restore --staged file`
  Discard unstaged file edits       `git restore file`
  Safely reverse a commit           `git revert COMMIT_ID`
  Temporarily stash work            `git stash push -m "message"`

## Recommended daily workflow

``` bash
git status
git pull
# Make and test your changes
git diff
git add path/to/changed-file
git diff --staged
git commit -m "Describe the change"
git push
```

Before running any command that discards changes, rewrites history, or
force-pushes, stop and check what it will affect.
