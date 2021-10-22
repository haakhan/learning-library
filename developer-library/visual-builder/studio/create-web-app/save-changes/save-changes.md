# Save a Web App's Changes to a Remote Branch

## Introduction

This lab shows you how to save a web application's changes from your local branch to a remote branch, so others can view your work.

Estimated Lab Time: 10 minutes

### Background
While developing the HR web application, you might have noticed a yellow dot in the header next to your Git repository:

![](images/git_changes_badge.png)

This dot indicates you've made changes in your local branch that haven't been saved to the remote branch. It's important to save your changes as often as you can, but first, let's review a few concepts.

When you first created a workspace, you created a new branch called `hrbranch`, which was a copy of the default branch (`main`) in the project’s Git repository and contained the same set of source files. Since then, all the changes you've made to the HR web app have been automatically saved to `hrbranch`, but these changes are not visible to others because `hrbranch` is local to your workspace. To let others view your changes, you'll need to save your changes from the local branch in your workspace to a branch in a remote repository.

Saving changes to a remote branch is a two-step process: _commit_ and _push_. The first step you'll do is "commit". A commit groups the files in your local branch that you want to save to the remote branch and provides a description of the group. Next, you'll "push" your changes. A push saves all the files in the groups that you've "committed" to the remote branch.

Once you commit and push your changes, all the changes from your local `hrbranch` become available to others in your project through the remote `hrbranch`.

### Prerequisites

This lab assumes you have:
* A Chrome browser
* All previous labs successfully completed

## Task 1: Commit Changes in a Local Branch
Let's group the changes you've made so far in your local branch for a commit. Ideally, you'll commit your changes as often as you can, so you have a string of commits with messages that clearly describe your updates.

1. Click the Git repository menu in the header and select **Commit**.

  ![](images/commit_menu.png " ")

2. In the Commit dialog box, enter a message that describes your changes and click **Commit**.

    ![](images/commit.png " ")

    A successful message appears on the page. Click ![Close message icon](images/x_icon.png) to close the message.

## Task 2: Push Changes to a Remote Branch

Push your commits from the local branch in your workspace to the remote branch.

1.  Click the Git repository menu and select **Push**.
2.  In the Push dialog box, you'll see 1 commit ready to be pushed from your local branch to the remote branch. Click **Push Changes**.

    ![](images/push_changes.png " ")

    When the successful message appears, click ![Close message icon](images/x_icon.png).

## Task 3: View Changes in the Remote Branch

Now that your changes have been pushed, let's check them in the remote `hrbranch`.

1. Click **Git History** at the bottom of your application window to view a summary of your push operation.

   ![](images/git_history.png " ")

   The Git History panel lists all your Git actions and their results and is useful to keep track of what you've done in your workspace. Click ![Close message icon](images/x_icon.png) when you are done.

2.  Now click **Go to project page** ![Go to Project Page icon](images/go_to_project_home_icon.png) in the header to return to the project's home page.

3.  Click **Git** ![Git icon](images/git_icon.png) in the left navigation.

   You'll see your changes added to the remote `hrbranch`, indicated by your last commit message.

    ![](images/git_view_hrbranch.png " ")

    Click the **Logs** tab to see all commits to the remote branch.

    ![](images/git_view_hrbranch_logs.png " ")

    Now if a teammate (for example, Clara Coder) wanted to work on this web application, she could use the **Clone From Git** option on the Workspaces page to clone `hrbranch` in her workspace, then use it as a base for her updates.

    You may now [proceed to the next lab](#next).


## Acknowledgements
* **Created By/Date** - Sheryl Manoharan, VB Studio User Assistance, October 2021
<!--* **Last Updated By** - October 2021 --!>
