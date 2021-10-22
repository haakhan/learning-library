# Share a Web App

## Introduction

This lab shows how you can share your web app with others using VB Studio.

Estimated Lab Time: 10 minutes

### Background
So far in this workshop, you've built the HR web application to show employees, their departments, and locations. You've also added navigation between the different pages and buttons to view, edit, and delete employee records and departments. Now that your work in the Designer is more or less complete, you can share the application with your team and ask for feedback.

Sharing an application, much like the preview option you've used in previous tutorials, lets you try out the application without committing its code to the project's Git repository (in this case, the changes you've made since your last push). But unlike a preview, which is visible only to you, a share action deploys your application to the VB instance associated with your development environment and creates a URL that you can pass along to your team. Your team can then test the behavior of your shared application and identify where it can be improved.

You can share your application as many times as you want to let your teammates test your changes and make sure the application works as expected.

### Prerequisites

This lab assumes you have:
* A Chrome browser
* All previous labs successfully completed

## Task 1: Share the Application

Share the HR web application you've created to create a URL that your team can use to try out the application.

1.  If necessary, click **Workspaces** ![Workspaces icon](images/vbs_workspaces_icon.png)and **HR Visual Application** in the Workspaces table to open your workspace.
2.  Click **Menu** ![Options menu icon](images/options_header_menu.png) in the header and select **Share**.

    ![](images/share.png " ")

3.  In the Share Visual Application dialog box, you'll see the URL that the hrwebapp will be shared to. (If you want, you can click the Copy icon to copy this URL, but we'll see how to get the URL after the application is shared.) Select **Use development data (my workspace)** to copy Department, Location, and Employee data from your workspace to your development environment's VB instance. Click **Share**.

    ![](images/share_application.png " ")

    A brief confirmation appears, and the application is deployed to your VB instance.


## Task 2: View the Shared Application

Now that you've shared your application, you need to get its URL so you can pass it along to your team. You do this by opening the application itself, or by copying the URL when you shared the application. Remember that your team members will need the proper credentials to view your shared application.

1.  Click **Menu** ![Options menu icon](images/options_header_menu.png) and select **Open Shared Applications**. If the option does not appear or is not active, it means your application is not yet fully deployed. Wait a while and try again.

    ![](images/open_shared_application.png " ")

    The shared application opens in a new browser tab. It includes all the changes you've made in your workspace, even those that were not pushed to the remote branch; it also displays data from your workspace.

    ![](images/open_shared_application_result.png " ")

2.  Make a note of the application's URL to share with your team, then close the browser tab.
3.  To view the same shared application now deployed to your development environment, click **Go to Project page** ![Go to Project Page icon](images/go_to_project_home_icon.png) in the header, then click **Environments** ![Environments icon](images/vbs_environments_icon.png) and **Deployments**. Expand **tutorial-hr-project** to view the shared application in your list of deployments.

    ![](images/shared_deployment.png " ")

    If you click **hrwebapp**, the application opens in a new browser tab, similar to the shared application view from within the Designer. When you've finished using the application, close the browser tab.

    Project team members like Clara Coder can also open the shared application from the list of deployments, as long as their membership includes access to the Environments page.

    You may now [proceed to the next lab](#next).


## Acknowledgements
* **Created By/Date** - Sheryl Manoharan, VB Studio User Assistance, October 2021
<!--* **Last Updated By** - October 2021 --!>
