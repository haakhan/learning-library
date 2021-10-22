# Constraining AUDIT POLICY and NOAUDIT POLICY SQL Commands with Oracle Database Vault Command Rules

## Introduction

### Objectives

### Prerequisites

## Task 1: Setup Oracle Database Vault

1. Execute the `setup_DV_CDB1.sh` script to create and enable Oracle Database Vault in CDB1.

    ```
    $ <copy>$HOME/labs/19cnf/setup_DV_CDB1.sh</copy>
    ```
## Task 2: Enable Audit Policy
1. Log into CDB1

    ```
    $ <copy>sqlplus system/Ora4U_1234@PDB1</copy>
    ```
2. Create the required audit policies.

    ```
    SQL> <copy>CREATE AUDIT POLICY pol1 ACTIONS SELECT ON hr.employees;</copy>
    Audit policy created.
    ```
3. Enable audit policy.

    ```
    SQL> <copy>AUDIT POLICY pol1</copy>
    Audit succeeded.
    ```
## Task 2: Create command rule
1. Log into PDB1 as `c##sec_admin`, this user was creating during the configuration of Oracle Database Vault.

    ```
    SQL> <copy>CONNECT c##sec_admin/Ora4U_1234@PDB1</copy>
    Connected.
    ```
2. Create a command rule that forbids users that are not `SYS` or `SYSTEM` from using the `AUDIT POLICY` and `NOAUDIT POLICY` commands in any circumstance and in PDB1. First, create a rule set to which you will associate the `Is Database Administrator` rule that checks whether the user executing a `NOAUDIT POLICY` command is granted the `DBA` role.

   ```
   SQL> <copy>EXEC dvsys.DBMS_MACADM.CREATE_RULE_SET( -
            rule_set_name    => 'Check_user', - 
            description      => 'Check user', -
            enabled          => DBMS_MACUTL.G_YES, -
            eval_options     => DBMS_MACUTL.G_RULESET_EVAL_ANY,-
            audit_options => DBMS_MACUTL.G_RULESET_AUDIT_FAIL,-
            fail_options  => DBMS_MACUTL.G_RULESET_FAIL_SILENT,-
            fail_message     => '',-
            fail_code        => '',-
          handler_options => DBMS_MACUTL.G_RULESET_HANDLER_OFF,-
            handler          => '',-
            is_static        => TRUE,-
            scope            => DBMS_MACUTL.G_SCOPE_LOCAL)</copy>
            > > > > > > > >  > > > > > > > > 
    PL/SQL procedure successfully completed.
   ```
3. Associate the predefined `Is SYS or SYSTEM User` rule to the ruleset.

    ```
    SQL> <copy>EXEC dvsys.DBMS_MACADM.ADD_RULE_TO_RULE_SET( -
             rule_set_name  => 'Check_user',-
            rule_name      => 'Is SYS or SYSTEM User')</copy>
            > > > > > >
    PL/SQL procedure successfully completed.
    ```
4. Create the command rule.

    ```
    SQL> EXEC dvsys.DBMS_MACADM.CREATE_COMMAND_RULE( -
          command       => 'AUDIT POLICY', -
          rule_set_name => 'Check_user',-               
          object_owner  => '%', -
          object_name   => 'POL1',-
          enabled       => DBMS_MACUTL.G_YES, -
          scope         => DBMS_MACUTL.G_SCOPE_LOCAL)
    > > > > > >
    PL/SQL procedure successfully completed.
    ```
## Task 3: Drop the audit policy as the `SYSTEM` user
1. Log in to PDB1 as `SYSTEM`.

    ```
    SQL> <copy>CONNECT system/Ora4U_1234@pdb1</copy>
    Connected.
    ```
2. Disable the audit policy.

    ```
    SQL> <copy>NOAUDIT POLICY pol1;</copy>
    Noaudit succeeded.
    ```
3. Drop the audit policy.

    ```
    SQL> <copy>DROP AUDIT POLICY pol1;
    Audit Policy dropped.
    ```
4. The previous step works because, in our rule set, we dictated that only `SYS` and `SYSTEM` users should be allowed to modify the `pol1` audit policy.
## Task 4: Create a new user with `DBA` privileges
1. Log into PDB1 as `c##accts_admin`, this account was created when you setup Oracle Database Vault.

    ```
    SQL> <copy>CONNECT c##accts_admin/Ora4U_1234@PDB1;</copy>
    Connected.
    ```
2. Create a DBA junior and grant the user the `DBA` role in PDB1.

    ```
    SQL> <copy>CREATE USER dba_junior IDENTIFIED BY Ora4U_1234;</copy>
    User created.
    ```
3. Grant the `DBA` privilege to `dba_junior`.

    ```
    SQL> <copy>GRANT dba TO dba_junior;
    Grant succeeded.</copy>
    ```
## Task 5: Create and attempt to modify a new audit policy
1. Connect to PDB1 as `dba_junior` and create an audit policy.

    ```
    SQL> <copy>CONNECT dba_junior/Ora4U_1234@PDB1
    Connected.</copy>
    ```
2. Create new audit policy.

    ```
    SQL> <copy>CREATE AUDIT POLICY pol1 ACTIONS SELECT ON hr.employees;</copy>
    Audit policy created.
    ```
3. Enable `AUDIT` on `pol1`.

    ```
    SQL> <copy>AUDIT POLICY pol1;</copy>

    ERROR at line 1:
    ORA-47400: Command Rule violation for AUDIT POLICY on POL1


    ```
## Task 6: Attempt to alter the audit policy as the Database Vault owner.
1. Attempt to execute `NOAUDIT` on `pol1` as `c##sec_admin`. First, connect to PDB1 as `c##sec_admin`.

    ```
    SQL> <copy>CONNECT c##sec_admin@PDB1</copy>
    ```
2. Enable `NOAUDIT` on `pol1`.

    ```
    SQL> <copy>NOAUDIT POLICY pol1;</copy>
    ```
3. Although `c##sec_amdin` is the Database Vault owner, it cannot disable the `AUDIT POLICY` because of the command rule we established earlier.

## Task 7: Alter the audit policy as the `SYSTEM` user

1. Drop the audit policy as the `SYSTEM` user. Log into PDB1 as the `SYSTEM` user.

    ```
    SQL> <copy>CONNECT system/Ora4U_1234@PDB1</copy>
    Connected.
    ```
2. Activate `NOAUDIT` on `pol1`.

    ```
    SQL> <copy>NOAUDIT POLICY pol1;</copy>

    Noaudit succeeded.
    ```
3. Drop the audit policy.

    ```
    SQL> <copy>DROP AUDIT POLICY pol1;</copy>
    ```
## Task 8: Clean your environment
1. Clean your environment.

    ```
    $ <copy>$HOME/labs/19cnf/disable_DV_CDB1.sh</copy>
    ```
   