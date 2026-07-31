Setting this entire architecture up 100% natively on your phone is
completely doable. Since you are building it directly on mobile, the
trick is avoiding the clunky web-based script editors on a small screen
and executing your file indexing right inside your phone's storage.

## **Step 1: Initialize the Automated Script Prompt (Via Mobile Browser)**

Google Apps Script does not have a dedicated mobile app, but you can
configure it via Chrome or Safari on your phone using **Desktop Mode**.

1.  Open your mobile browser, tap the menu settings (three dots or
    > "aA"), and select **"Request Desktop Site"**.

2.  Navigate to Google Apps Script Dashboard and log in. \[1\]

3.  Tap **New Project**. Clear the empty editor and paste the automation
    > script provided previously. \[1\]

4.  To get your Folder IDs entirely from your phone, open the **Google
    > Drive app**:

    - Navigate to your folder, tap the three dots next to it, select
      > **Copy Link**.

    - Paste that link anywhere temporary. The folder ID is the long
      > string of letters and numbers right after folders/ in the URL
      > string.

5.  Paste those folder IDs into the script, tap the **Save (Floppy
    > Disk)** icon, and then tap **Run**. \[1, 2\]

6.  Tap the **Alarm Clock icon (Triggers)** on the left rail menu. Set
    > exportGoogleDocs to launch on a **Time-driven** event every hour.
    > \[2, 3\]

Your phone can now be turned completely off—Google's servers will run
this process in the cloud automatically.

## **Step 2: Set Up Local Terminal Indexing on Your Phone**

Because mobile operating systems sandbox files, an external agent
framework cannot cleanly run a terminal over your Google Drive storage
folder. You can solve this by creating a localized sandbox environment
directly on your device.

## **1. Download a Native Terminal (Android/iOS)**

- 

- **Android:** Download **Termux**. (Do not get it from the Play Store
  > as that version is outdated; install it via the [<u>F-Droid Client
  > App</u>](https://f-droid.org/) or download the direct Termux APK
  > file).

- **iOS:** Download **iShane** or **a-Shell** from the App Store. These
  > apps provide an offline Unix terminal sandbox directly on an iPhone
  > or iPad. \[4, 5, 6\]

- 

## **2. Give the Terminal Storage Access**

Once you open your phone's terminal app, you must permit it to view your
local file folders.

- 

- **On Android (Termux):** Type this command and press enter:  
  > termux-setup-storage  
  > *Tap "Allow" on the system popup prompt that appears.*

- **On iOS (a-Shell):** Type pickFolder to open the native Files app UI
  > and select the target workspace directory. \[4\]

- 

## **3. Install Git and Your Indexer Tooling**

Inside your mobile terminal terminal prompt, update your core packages
and pull the required search packages by running:

> pkg update && pkg upgrade -y  
> pkg install grep git nodejs -y

## **Step 3: Run the Agent / Prompt Commands Natively**

Your phone now houses a fully functional file indexer. You have two ways
to execute your workflows: \[4\]

## **Method A: Manual Phone Indexing ("Grep This")**

You can download the files that your Google Sheet automatically
generated into your phone's local storage. Open your phone's terminal
app, navigate to your download directory, and run native search
patterns: \[7\]

> *\# Navigate to your phone's shared downloads folder*  
> cd ~/storage/shared/Download/AgentWorkspace  
>   
> *\# Search all your .jsonl and .md text files for a concept*  
> grep -r "your target keyword" .

## **Method B: Mobile MCP Agent Connection**

If you want an AI agent to do the heavy lifting from your phone instead
of typing terminal lines yourself:

1.  Initialize the node project right inside your phone's terminal
    > workspace:  
    > npm install -g @hasna/skills && skills auth signup

2.  Drop your master skills.md file layout directly into that local
    > directory.

3.  Run the mobile framework runtime daemon directly inside your phone's
    > terminal:  
    > skills run your-custom-agent-profile --theme "mobile indexing"

Would you like to build an automated **shell loop command** you can run
on your phone to quickly pull files from Drive straight into your
terminal workspace, or do you want to start writing out the structural
logic for your **skills.md tool profiles**?

\[1\]
[<u>https://developers.google.com</u>](https://developers.google.com/workspace/forms/api/guides/apps-script-setup)

\[2\]
[<u>https://www.linkedin.com</u>](https://www.linkedin.com/posts/chaddavis1_google-apps-script-for-accountants-the-use-activity-7343281477184299010-tuEr)

\[3\]
[<u>https://support.google.com</u>](https://support.google.com/appsheet/answer/12008053?hl=en)

\[4\]
[<u>https://www.youtube.com</u>](https://www.youtube.com/watch?v=M1DSUl8HlP8)

\[5\]
[<u>https://wiki.termux.com</u>](https://wiki.termux.com/wiki/Installing_from_F-Droid)

\[6\]
[<u>https://forum.f-droid.org</u>](https://forum.f-droid.org/t/how-to-install-termux-from-f-droid/31804)

\[7\]
[<u>https://askubuntu.com</u>](https://askubuntu.com/questions/55325/how-to-use-grep-command-to-find-text-including-subdirectories)
