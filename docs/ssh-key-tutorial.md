# SSH Keys for Developers (Ubuntu/WSL + GitHub)

## 1. What is SSH?

SSH (Secure Shell) authenticates your computer securely with services such as GitHub, without entering your GitHub password for every Git operation.

An SSH key pair contains:

- **Private key** (`~/.ssh/id_ed25519`): stays on your machine; never share it.
- **Public key** (`~/.ssh/id_ed25519.pub`): add this to GitHub or another service.

## 2. Install and generate a key

Check whether SSH is installed:

```bash
ssh -V
```

If needed:

```bash
sudo apt update
sudo apt install openssh-client
```

Generate an Ed25519 key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press **Enter** to accept the default file path. Set a strong passphrase when prompted.

Files created:

```text
~/.ssh/id_ed25519       # Private key — keep secret
~/.ssh/id_ed25519.pub   # Public key — safe to register
```

If the default key already exists, don't overwrite it unless you intend to replace it. You can choose a different filename when prompted.

## 3. Add the key to your SSH agent

Start the agent:

```bash
eval "$(ssh-agent -s)"
```

Load the private key:

```bash
ssh-add ~/.ssh/id_ed25519
```

Check loaded keys:

```bash
ssh-add -l
```

## 4. Add your public key to GitHub

Print the public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Optional: copy it to the Windows clipboard from WSL:

```bash
clip.exe < ~/.ssh/id_ed25519.pub
```

Then:

1. Open <https://github.com/settings/keys>.
2. Select **New SSH key**.
3. Give it a title (for example, `Ubuntu WSL Laptop`).
4. Choose **Authentication Key**.
5. Paste the full contents of `id_ed25519.pub` and save.

**Never paste or upload the private key.**

## 5. Test SSH authentication

```bash
ssh -T git@github.com
```

On the first connection, verify the host fingerprint against GitHub's official documentation before accepting it. Successful authentication prints a greeting such as:

```text
Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.
```

This is expected: GitHub supports Git operations over SSH, not an interactive shell.

## 6. Use SSH for a repository

Clone with the repository's SSH URL:

```bash
git clone git@github.com:OWNER/REPOSITORY.git
```

For an existing repository, inspect and change its remote:

```bash
git remote -v
git remote set-url origin git@github.com:OWNER/REPOSITORY.git
git remote -v
```

Replace `OWNER/REPOSITORY` with the actual repository path. If the remote starts with `https://`, it is using HTTPS rather than SSH.

## 7. Useful commands

```bash
ls -la ~/.ssh/                  # List SSH files
cat ~/.ssh/id_ed25519.pub       # Display public key
ssh-add -l                      # List keys loaded in agent
ssh-add ~/.ssh/id_ed25519       # Load private key into agent
ssh -T git@github.com            # Test GitHub authentication
ssh -vT git@github.com           # Debug connection/authentication
```

## 8. Troubleshooting

- **`Permission denied (publickey)`**: confirm the public key is registered with the right GitHub account and the matching private key is available.
- **Agent connection error**: run `eval "$(ssh-agent -s)"`, then `ssh-add ~/.ssh/id_ed25519`.
- **Git still uses HTTPS**: inspect `git remote -v` and change the remote to the SSH URL.
- **Wrong key is being used**: run `ssh -vT git@github.com` to inspect which keys SSH offers.
- **Key file not found**: check `ls -la ~/.ssh/` and confirm the filename.

## 9. Security essentials

- Never share, email, commit, or upload your private key.
- Use a passphrase and keep your machine account secure.
- If a key is exposed, remove its public key from GitHub and generate/register a replacement.
- Use separate keys for separate machines when practical.
- WSL and Windows have separate SSH directories by default (`~/.ssh` inside WSL is not the same as the Windows user's `.ssh` folder).
- Only accept a first-time server host key after verifying its fingerprint through a trusted source.

Official reference: <https://docs.github.com/en/authentication/connecting-to-github-with-ssh>
