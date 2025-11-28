---
layout: default
title: "Lab 1: Implement Zero Trust Security Controls"
parent: Module 1 - Zero Trust Security
nav_order: 3
---

# Lab 1: Implement Zero Trust Security Controls

{: .no_toc }

{: .warning }
> **🚧 Lab Under Development**  
> This lab content is complete but hands-on exercises are currently being validated and refined.  
> **Expected Release:** Q1 2026  
> You can review the lab steps and prepare your environment in advance.

## Overview

In this hands-on lab, you will implement Zero Trust security controls in a sovereign cloud environment. You will configure identity-based access controls, device compliance policies, conditional access rules, and set up monitoring for a production-like deployment.

**Duration:** 2-3 hours  
**Difficulty:** Intermediate-Advanced  
**Prerequisites:** Level 200 completion, Azure subscription access

---

## Learning Objectives

Upon completion, you will be able to:

- ✅ Configure Entra ID for Zero Trust authentication
- ✅ Implement device compliance policies
- ✅ Create and test conditional access rules
- ✅ Set up MFA for users
- ✅ Configure role-based access control (RBAC)
- ✅ Implement Azure Audit logging for compliance
- ✅ Monitor and respond to access anomalies

---

## Lab Architecture

```text
External User Request
    ↓
Entra ID (Identity Verification + MFA)
    ↓
Device Compliance Check
    ↓
Conditional Access Rules
    ↓
Application Access (with audit logging)
    ↓
Azure Monitor (Compliance & Anomaly Detection)
```

---

## Lab Scenario

**Company:** TechCorp Defense Solutions  
**Environment:** Sovereign Cloud deployment (connected mode)  
**Requirement:** Implement Zero Trust for development team accessing classified data  
**Compliance:** FedRAMP High

**Users:**

- 5 developers
- 3 security admins
- 2 application admins

**Resources:**

- Development environment (Azure VMs)
- Sensitive data storage (encrypted blob storage)
- Audit logs (Log Analytics workspace)

**Constraints:**

- All access must use MFA
- Devices must be compliant (encryption, patches)
- Access requires explicit business justification
- All activity must be logged for audit

---

## Exercise 1: Set Up Identity & Authentication (1 hour)

### Task 1.1: Create User Accounts

1. **Create users in Entra ID:**
   - Access Azure Portal → Entra ID → Users
   - Create 10 test users (developers + admins)
   - Assign temporary passwords
   - Require password change on first login

2. **Configure Self-Service Password Reset (SSPR):**
   - Entra ID → Password reset
   - Enable SSPR for all users
   - Require MFA for SSPR
   - Send test password reset email

3. **Verification:**
   - [ ] 10 users created and visible in Entra ID
   - [ ] SSPR configured and working
   - [ ] Users can reset password and confirm MFA

### Task 1.2: Implement Multi-Factor Authentication

1. **Enable per-user MFA:**
   - Entra ID → Multi-Factor Authentication
   - Select 5 developer users
   - Enable MFA: Require
   - Test MFA sign-in

2. **Configure MFA Methods:**
   - Require Microsoft Authenticator app
   - Enable phone call as backup
   - Disable weaker methods

3. **Verification:**
   - [ ] MFA enforced for selected users
   - [ ] Sign-in requires MFA
   - [ ] Test backup MFA method

### Task 1.3: Implement Passwordless Authentication

1. **Enable Passwordless Sign-In:**
   - Entra ID → Security → Passwordless methods
   - Enable Windows Hello for Business
   - Enable FIDO2 security keys
   - Test passwordless sign-in

2. **Verification:**
   - [ ] Passwordless methods configured
   - [ ] At least one user can sign in passwordless
   - [ ] Fallback to password still works

---

## Exercise 2: Device Compliance (1 hour)

### Task 2.1: Create Device Compliance Policies

1. **Create Device Compliance Policy:**
   - Intune → Device compliance → Policies
   - Create policy: "FedRAMP Compliance Policy"
   - Configure rules:
     - OS version minimum (Windows 10 21H2+)
     - BitLocker encryption: Required
     - Antivirus: Required (Windows Defender)
     - Firewall: Required
     - Security updates: Required (auto-install)

2. **Assign Policy:**
   - Target: All devices in group
   - Assignment: Development Team group
   - Test with lab device

3. **Verification:**
   - [ ] Policy created and assigned
   - [ ] Lab device shows compliant/non-compliant status
   - [ ] Remediation guidance provided for non-compliant devices

### Task 2.2: Configure Conditional Access for Non-Compliant Devices

1. **Create Access Rule:**
   - Entra ID → Conditional Access → New policy
   - Name: "Block non-compliant devices"
   - Conditions:
     - Users: Development Team
     - Resources: Development Applications
     - Device compliance: Require compliant device
   - Controls:
     - Block access
   - Enable policy

2. **Verification:**
   - [ ] Policy created
   - [ ] Non-compliant device cannot access protected apps
   - [ ] Compliant device can access

### Task 2.3: Monitor Device Health

1. **Set up Device Health Monitoring:**
   - Intune → Device compliance → Monitor
   - Review compliance reports
   - Set up non-compliance alerts

2. **Verification:**
   - [ ] Compliance reports visible
   - [ ] Non-compliant devices identified
   - [ ] Alerts configured

---

## Exercise 3: Conditional Access Policies (1 hour)

### Task 3.1: Create Location-Based Access Policy

1. **Create Policy:**
   - Entra ID → Conditional Access → New policy
   - Name: "Location-Based Access"
   - Conditions:
     - Users: All developers
     - Resources: Sensitive data storage
     - Locations: Corporate office + approved VPN
   - Controls:
     - Require MFA
     - Require compliant device
   - Enable policy

2. **Test:**
   - Sign in from corporate network (should allow)
   - Simulate sign-in from unexpected location (should require MFA or block)

3. **Verification:**
   - [ ] Policy blocks unauthorized locations
   - [ ] Authorized locations grant access
   - [ ] MFA required from edge locations

### Task 3.2: Create Risk-Based Access Policy

1. **Create Policy:**
   - Entra ID → Conditional Access → New policy
   - Name: "High-Risk Access Prevention"
   - Conditions:
     - Sign-in risk: High
     - Users: All users
   - Controls:
     - Require MFA
     - Require password change
     - Block access (high risk)
   - Enable policy

2. **Verification:**
   - [ ] Policy recognizes high-risk sign-ins
   - [ ] Appropriate controls applied

### Task 3.3: Create Time-Based Access Policy

1. **Create Policy:**
   - Entra ID → Conditional Access → New policy
   - Name: "Business Hours Only Access"
   - Conditions:
     - Users: Contractors
     - Time: Outside 8am-6pm Mon-Fri
   - Controls:
     - Block access
   - Enable policy

2. **Verification:**
   - [ ] Access allowed during business hours
   - [ ] Access blocked after hours

---

## Exercise 4: Role-Based Access Control (1 hour)

### Task 4.1: Create Custom Roles

1. **Create Developer Role:**
   - Azure Portal → Subscriptions → Access Control (IAM)
   - Create custom role: "Development Contributor"
   - Permissions:
     - Read all resources
     - Create/modify/delete VMs
     - Write to storage
     - Exclude: Delete resource groups, modify RBAC
   - Assign to Development Team group

2. **Create Security Admin Role:**
   - Create custom role: "Security Monitor"
   - Permissions:
     - Read all resources
     - Read audit logs
     - Read compliance reports
     - No write access
   - Assign to Security Team group

3. **Verification:**
   - [ ] Custom roles created
   - [ ] Roles assigned to groups
   - [ ] Permissions enforced correctly

### Task 4.2: Implement Just-In-Time (JIT) Access

1. **Enable JIT for VMs:**
   - Azure Portal → Security Center → Just-in-time VM access
   - Enable JIT for 2-3 development VMs
   - Configure: RDP access, 4-hour window, approval required

2. **Request and Approve Access:**
   - User requests access to VM
   - Admin reviews and approves request
   - Access granted for specified window
   - Verify audit log entry

3. **Verification:**
   - [ ] JIT enabled on VMs
   - [ ] Access requests visible
   - [ ] Audit log records access

---

## Exercise 5: Audit Logging & Compliance (1 hour)

### Task 5.1: Configure Azure Audit Logging

1. **Enable Audit Logging:**
   - Azure Portal → Subscriptions → Activity Log
   - Verify audit logs are being collected
   - Configure log retention: 90 days minimum

2. **Export Logs to Log Analytics:**
   - Create Log Analytics workspace
   - Configure diagnostic settings to export audit logs
   - Create dashboard showing activity

3. **Verification:**
   - [ ] Audit logs visible in Activity Log
   - [ ] Logs exported to Log Analytics
   - [ ] Dashboard created showing activity

### Task 5.2: Create Compliance Reports

1. **Generate Access Reports:**
   - Entra ID → Reports → Sign-ins
   - Filter by user, app, result
   - Document access patterns

2. **Generate Audit Reports:**
   - Log Analytics → Create query for policy changes
   - Run quarterly compliance report
   - Document findings

3. **Verification:**
   - [ ] Reports generated
   - [ ] Compliance data captured
   - [ ] Patterns identified

### Task 5.3: Set Up Alerts

1. **Create Alerts:**
   - Azure Monitor → Alerts → New alert
   - Conditions:
     - Multiple failed authentication attempts (5+ in 10 min)
     - Admin role assignment
     - Sensitive data access outside hours
   - Action: Send email notification

2. **Test Alerts:**
   - Trigger failed authentication alert
   - Verify email notification
   - Document alert behavior

3. **Verification:**
   - [ ] Alerts configured
   - [ ] Alerts trigger correctly
   - [ ] Notifications working

---

## Exercise 6: Monitoring & Response (1 hour)

### Task 6.1: Investigate Anomalous Activity

1. **Scenario:** Detect unusual access pattern
   - Review access logs
   - Identify: User accessing from unusual location
   - Check: Device compliance, MFA, risk level
   - Determine: Legitimate or suspicious?

2. **Response:**
   - If suspicious:
     - Block user session
     - Force password reset
     - Require re-authentication
     - Notify user
   - Document incident

3. **Verification:**
   - [ ] Anomaly identified
   - [ ] Appropriate response taken
   - [ ] Incident documented

### Task 6.2: Review Access Entitlements

1. **Conduct Access Review:**
   - Review: Who has access to what?
   - Verify: Access matches business need
   - Identify: Orphaned accounts or excessive access
   - Remediate: Remove unnecessary access

2. **Documentation:**
   - Create access review report
   - Document decisions
   - Plan follow-up for next quarter

3. **Verification:**
   - [ ] Access review completed
   - [ ] Entitlements validated
   - [ ] Excessive access removed

---

## Success Criteria

You have successfully completed this lab when:

- ✅ Users can authenticate with MFA
- ✅ Device compliance is enforced (non-compliant devices blocked)
- ✅ Conditional access policies are working
- ✅ Role-based access control is enforced
- ✅ JIT access is working for VMs
- ✅ All access is logged and auditable
- ✅ Alerts are configured and working
- ✅ Compliance reports can be generated

---

## Lab Deliverables

1. **Entra ID Configuration Document:**
   - User accounts created
   - MFA methods configured
   - Passwordless auth enabled

2. **Device Compliance Report:**
   - Compliance policies created
   - Devices assessed
   - Remediation status

3. **Conditional Access Report:**
   - All policies listed
   - Test results documented
   - Edge cases covered

4. **RBAC Documentation:**
   - Custom roles defined
   - Assignments documented
   - JIT access configured

5. **Compliance Report:**
   - Audit logs and retention
   - Alerts configured
   - Sample incidents investigated

---

## Troubleshooting

**Issue:** User blocked by conditional access policy  
**Resolution:** Check policy conditions, device compliance, location, risk level

**Issue:** MFA not working  
**Resolution:** Verify MFA method registered, app installed, backup methods configured

**Issue:** Audit logs not showing activity  
**Resolution:** Verify diagnostic settings, log retention, query syntax

**Issue:** Alert not triggering  
**Resolution:** Check alert conditions, verify logs are being collected, test manually

---

## Next Steps

1. Review [Module Summary →](zero-trust)
2. Continue to [Module 2: Azure Local at Scale - Connected →](../azure-local-advanced-connected)
3. Complete all Level 300 modules before final assessment

---

**Lab Created:** October 2025  
**Last Updated:** October 2025
