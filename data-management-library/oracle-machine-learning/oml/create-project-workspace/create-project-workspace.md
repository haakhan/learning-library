# Oracle® Cloud Create Projects and Workspaces in Oracle Machine Learning Notebooks
## Before You Begin

This lab walks you through the steps to create a project and a workspace in Oracle Machine Learning Notebooks.

>**Note:** The initial workspaces and the default project are created by the Oracle Machine Learning service automatically when you log in to Oracle Machine Learning Notebooks for the first time. The term default applies to the last project that you work on, and it is stored in the browser cache. If you clear the cache, then there would be no default project selected. Then you must select a project to work with notebooks.

This lab explains the steps to

* Create an Oracle Machine Learning user
* Sign into Oracle Machine Learning user interface
* Create your own project, and optionally your workspace.

This lab takes approximately 10 minutes to complete.

### Background
A project is a container for storing your notebooks and other objects such as dashboards and so on. A workspace is a virtual space where your projects reside, and multiple users with the appropriate permission type can work on different projects. While you may own many projects, other workspaces and projects may be shared with you.

### What Do You Need?

Access to your Oracle Machine Learning Notebooks account

## Create an Oracle Machine Learning user

An administrator creates a new user account and user credentials for Oracle Machine Learning in the User Management interface.

>**Note:** You must have the administrator role to access the Oracle Machine Learning User Management interface.

To create a user account:

1. Sign in to your OCI account, click the hamgurger on the left to open the left navigation pane, and click **Autonomous Data Warehouse**.

	![Oracle Autonomous Data Warehouse](images/adw.png)


2. Click on an Autonomous Database instance.   

	![Oracle Autonomous Data Warehouse](images/adb_instance.png)


3. On the Autonomous Database Details page, click **Service Console**.

	![Oracle Autonomous Data Warehouse](images/service-console.png)


4. On the Service Console click **Administration**.

	![Oracle Autonomous Data Warehouse](images/administration.png)


5. Click **Manage Oracle ML Users** to open the Oracle Machine Learning User Administration page.

	![Oracle Autonomous Data Warehouse](images/manage_oml_users.png)

6. On the Oracle Machine Learning User Administration Sign in page, enter the username and password to sign in.

	>**Note:** The username is ADMIN. The password is what is you have defined while provisioning the Autonomous Database instance.   

	![Oracle Machine Learning User Administration Sign in page](images/database_admin_signin.png)

7. Click **Create** on the Oracle Machine Learning User Administration page.

	![Oracle Autonomous Data Warehouse](images/oml_um_page.png)

7. On the Create User page, enter the following details to create the user:

	![Oracle Autonomous Data Warehouse](images/create_user.png)

	* **Username:** Enter a username for the account. Using the username, the user will log in to an Oracle Machine Learning instance.
	* **First Name:** Enter the first name of the user.
	* **Last Name:**  Enter the first name of the user.
	* **Email Address:** Enter the email ID of the user.
	* Select the option **Generate password and email account details to user. User will be required to reset the password on first sign in** to auto generate a temporary password and send an email with the account credentials to the user. If you select this option, you need not enter values in the Password and Confirm Password fields; the fields are grayed out.
	* **Password:** Enter a password for the user, if you choose to create a password for the user.
	>**Note:** This option is disabled if you select the **Generate password...** option to auto generate a temporary password for the user.

	* **Confirm Password:** Enter a password to confirm the value that you entered in the Password field. By doing so, you create the password for the user. The user can change the password when first logging in.

8. Click **Create**.

This completes the task of creating an Oracle Machine Learning user.

## Sign into Oracle Machine Learning Notebooks

A notebook is a web-based interface for data analysis, data discovery, data visualization, and collaboration. You create and run notebooks in Oracle Machine Learning Notebooks. You can access Oracle Machine Learning Notebooks from Autonomous Database.

1. From the tab on your browser with your ADW instance, click **Service Console**, then select **Development** on the left.

	![Development option in ADW Service Console](images/adw_development.png)


2. Click **Oracle Machine Learning Notebooks.**

	 ![Oracle Machine Learning Notebooks in ADW](images/oml_notebooks_dev.png)

3. Enter your user credentials and click **Sign in**.

	>**Note:** The credential is what you have defined while creating the Oracle Machine Learning user.

	![Oracle Machine Learning Notebooks Sign in page](images/omluser_signin.png)

4. Click **Notebooks** in the Quick Actions section.

	![Notebooks option in OML homepage](images/homepage_notebooks.png)

This completes the task of signing into Oracle Machine Learning user interface.



## Create Project in Oracle Machine Learning Notebooks

To create a project:
1. On the top right corner of the Oracle Machine Learning Notebooks home page, click the project workspace drop-down list. The project name and the workspace, in which the project resides, are displayed here. In this screenshot, the project name is `USER1 Project`, and the workspace name is `USER1 Workspace`. If a default project exists, then the name of the default project is displayed here. To choose a different project, click **Select Project**.

  ![new_project.png](images/new_project.png "new_project.png")

2. To create a new project, click **New Project**. The Create Project dialog box opens.

  ![create_workspace.png](images/create_workspace.png "create_workspace.png")


3. In the **Name** field, provide a name for your project.


4. In the **Comments** field, enter comments, if any.


5. To choose a different workspace, click the down arrow next to the **Workspace** field and select a workspace from the
  drop-down list. Your project `Project A` is assigned to the selected workspace. In this example, the `USER1 Workspace` is selected.

6. Click **OK**. This completes the task of creating a project and assigning it to a workspace. In this example, the assigned workspace is `USER1 Workspace`.




## Create Workspace in Oracle Machine Learning Notebooks
To create a workspace:

1. On the top right corner of the Oracle Machine Learning Notebooks home page, click the project workspace drop-down list and click **Select Project**. The Select Project dialog box opens.

  ![select_project.png](images/select_project.png "select_project.png")


2. In the Select Project dialog box, click **USER1 Workspace** and then click **Create**. The Create Project dialog box opens.

  ![select_project_create.png](images/select_project_create.png "select_project_create.png")

3. In the Create Project dialog box, enter `Project B` in the **Name** field, and click the plus icon next to the **Workspace** field. The Create Workspace dialog box opens.

  ![create_workspace_ab.png](images/create_workspace_ab.png "create_workspace_ab.png")

4. In the Create Workspace dialog box, enter Workspace A in the **Name** field.

  ![workspace_ab.png](images/workspace_ab.png "workspace_ab.png")

5. In the **Comments** field, enter comments, if any.


6. Click **OK.** This completes the task of creating your workspace, and brings you back to the Create Project dialog box.


7. In the Create Project dialog box, click **OK**. This brings you back to the Select Project dialog box. Here, you
   can view all the workspace and the projects in it. The project and workspace that you created in step 3 through 6 is listed in the Select Workspace dialog box, as shown in the screenshot here.

   ![select_project_workspace.png](images/select_project_workspace.png "select_project_workspace.png")

8. Click **OK.** This completes the task of creating a project and a workspace, and assigning the project to the workspace.


9. To delete a workspace, click **Manage Workspace** in the Project Workspace drop-down list.

10. In the Manage Workspace dialog box, select the workspace you want to delete and click **Delete**.
  This deletes the selected workspace along with all the projects in it.

  ![manage_workspace_delete.png](images/manage_workspace_delete.png "manage_workspace_delete.png")




## Acknowledgements

* **Author** : Mark Hornick, Sr. Director, Data Science / Machine Learning PM; Moitreyee Hazarika, Principal User Assistance Developer, Database User Assistance Development

* **Last Updated By/Date**: Moitreyee Hazarika, October 2021

See an issue?  Please open up a request [here](https://github.com/oracle/learning-library/issues).   Please include the workshop name and lab in your request.
