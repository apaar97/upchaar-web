### Unified Portal for Centrally Handled Application for Appointment Requisition (UPCHAAR)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
[![Requirements Status](https://requires.io/github/apaar97/UpchaarWeb/requirements.svg?branch=master)](https://requires.io/github/apaar97/UpchaarWeb/requirements/?branch=master)
[![GitHub issues](https://img.shields.io/github/issues/apaar97/UpchaarWeb.svg)](https://github.com/apaar97/UpchaarWeb/issues)
[![GitHub forks](https://img.shields.io/github/forks/apaar97/UpchaarWeb.svg)](https://github.com/apaar97/UpchaarWeb/network)
[![GitHub stars](https://img.shields.io/github/stars/apaar97/UpchaarWeb.svg)](https://github.com/apaar97/UpchaarWeb/stargazers)
[![GitHub license](https://img.shields.io/github/license/apaar97/UpchaarWeb.svg?color=blue)](https://github.com/apaar97/UpchaarWeb/blob/master/LICENSE)


#### Smart India Hackathon 2018 
#### Ministry of Health and Family welfare 
*Problem Statement: Improving appointment scheduling in the Hospitals*

A central portal for Patients, Doctors and Hospitals to manage and provide efficent healthcare. 

* Problems in current system
    
    * Difficulty in getting appointments in large tertiary care hospitals 
    * No mechanism present to inform patient if the same provider is available or not in the hospital on the scheduled date. 
    * Absence of process of rescheduling appointment with any other provider and for follow-ups the appointment scheduling system does not    generate any reminders to the patients
    * If patient discovers late about the follow-up visit he has to do the entire process of appointment scheduling again to get the appointments done. 
    * Lack of interface to link the current appointment system with the duty roster of the doctors

* About UPCHAAR portal

    * A appointment management system with provision for follow-up and rescheduling, with provision for SMS and app notifications
    * A reminder system wherein the patients and the doctors will be reminded of their appointments in advance so that the chances of appointment being missed are minimized.
    * Automatic rescheduling in cases of missed or periodic appointments.
    * Includes a provision for emergency requests wherein the user can bypass the system and avail services in critical situations.
    * Builds more trust among patients about the hospital and would also encourage patients to get timely follow-up visits done to improve their health status. 

* Tech Stack (Web)
    
    * Django 2.0 (Python >= 3.3)
    * DjangoRestFramework - Rest API 
    * Nexmo SMS Client (https://www.nexmo.com/)   
