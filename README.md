# LowkeySpots

## 👋 Introduction
  **_LowkeySpots_** is a social app that enables users to share customized spots with each other on personal, interactive maps. 

  ![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/58f7ff6f-5f11-4c60-b4d6-5afad15295e7)



  The **Goal** of this project was to offer a distraction-free platform tailored for efficiency and simplicity. Its clean interface and intuitive design make it effortless for users to navigate and share their adventures, whether they're tech-savvy or new to the platform. Ideal for friends and family, LowkeySpots provides a personalized space to curate and share memories, adding an exclusive touch to social sharing experiences.



## ⚙️ Tech Stack
LowkeySpots is a **full-stack** application built using the following technologies:

<div align="center">
    <img src="https://img.shields.io/badge/-TypeScript-black?style=for-the-badge&logoColor=white&logo=typescript&color=3178C6" alt="Typescript" />
       <img src="https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB" alt="React"/>
    <img src = "https://img.shields.io/badge/SASS-hotpink.svg?style=for-the-badge&logo=SASS&logoColor=white)" alt="SASS">
    <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
    <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgresSQL"/>
   <img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS"/>
   <img src = "https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white" alt="Google Cloud"/>
    <img src = "https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
</div>


Additionally, [**MapBox**](https://www.mapbox.com/) was used for rendering maps and retrieving geological data 


## 🧰 Features

### Adding Friends

You can see all your requests in the **Pending** tab. Here you can choose to accept or deny friend requests

![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/d7f63882-9c0a-4a9e-bd3a-5d89f04e70f4)


If accepted, you will be able to see each other as a friend on the **Friends** tab:

![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/c5f95f00-c7ef-4ddf-b635-c4b0534d442a)

When sending friend requests go to the **Add Friend** Tab:

![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/28a937ba-236e-4c01-921a-850f598841a1)


Type in the your friend's username and click Send Request:
![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/e6f2ed61-34a9-4e8e-aee2-fa506b952164)


If the username exists you will get this message:


![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/bc51cdc1-7400-4374-bb33-2037911eb5eb)


**Error Handling:**

_Username does not exist_

![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/fd5bef1e-b1f8-4efb-9ff9-accc776961ba)


_Already Friends_

![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/90752344-7398-407f-b3e5-aba3e3c38045)


_Request already sent_


![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/0d827305-cf62-455f-890a-b61ad7fb2705)





### Map Dashboard

This is your map dashboard. Here you will be able to see all the maps you have created

![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/f9a336bf-5b60-4c17-815e-7ca054494950)


In LowkeySpots, there are three different roles : **Admin**, **Collaborator**, and **Spectator**. These roles will be explained in further detail but for know all you need to know is that if you are an Admin then you can delete maps, which essentially removes all users who were part of the map. However, if you are a Collaborator or Spectator, you will have the option to leave the map. At the top you can see there is a filteration system for these roles 

To create a new map simply press the New Map button. You will then be prompted this window
![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/832040f9-0a77-4b1e-aef3-d9e56d657b7b)


Once created, your map will be in your dashboard!

### Using and Sharing maps

This is the map editior
![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/cd0f362a-158f-4c2d-a409-75d6742e72b7)


On the left is the **Marker Bar**, where you **Edit**, **View Photos**,  or **Delete**. Click on the name itself will fly to the marker

![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/edbbfd9c-25bb-4fd2-8f8d-63b41a3890dc)


When editing a spot you will be prompted this window. As you can see, you can change **Name, Description, Color,** and **Upload Photos**


![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/f0695414-d270-4bbd-9f64-0667e776d901)



You can view the gallery for the spot as well. Each spot can have up to 10 images:

![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/423c6872-ccc8-4474-9312-9c446f12cdb1)


![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/d56ae0cf-b891-43bc-8cf2-4da200ca168a)


To add people on the map simply press on **Add Friend**. You will be prompted this window where you can add them as a  Collaborator or Spectator


![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/92eed640-0896-400d-95b8-89a014ef342b)


Once you add them you can see them by pressing the **Member List** button. If needed, you can either remove or change the permissions of these members

![image](https://github.com/AkashSanthanam/LowkeySpots/assets/73759561/852a1cef-be70-45c5-9f14-7aebb490eb65)


 - A Collobarator is someone who can do everything an Admin can except for adding/removing members
 - A Spectator is someone who can only view the map along with markers and photos

An example where Spectators might be needed or helpful is for marathons which have very specific routes that can be displayed using markers. Obviously we would not want runners to change /edit the markers so we can add them as Spectators. 



## 🎨 Design 

The website has 3 pages: Homepage, Friend Page and Map Page
![FlowChart](FlowChart.png)

We also created a RESTful API by using Entity-Relatioship Database Design Concepts and created the following schema which includes the **User, Friend, Map,** and **Marker** base 


**USER**

| Field           | Type            | Description                                                   |
|-----------------|-----------------|---------------------------------------------------------------|
| `name`            | `string`          | *might need to hash User.name and request_id*                |
| `psswd`           | `string`          |                                                               |
| `email`           | `string`          |                                                               |
| `date_created`    | `DateTime object` |                                                               |
| `account_deleted` | `bool`            |                                                               |
| `map_count`       | `int`             |                                                               |
| `token`           | `hash`            |                                                               |

**FRIEND_REQUEST**

| Field       | Type            | Description                                                                |
|-------------|-----------------|----------------------------------------------------------------------------|
| `request_id`  | `int(chron)`      |                                                                            |
| `sender`      | `USER.name`       |                                                                            |
| `receiver`    | `USER.name`       |                                                                            |
| `status`      | `int`             | *0: pending \| 1: accepted \| 2: rejected \| 3: invalid request*          |

**USERS_RELATION**

| Field    | Type       | Description                                              |
|----------|------------|----------------------------------------------------------|
| `user_1`   | `USER.name`  |                                                          |
| `user_2`   | `USER.name`  |                                                          |
| `status`   | `int`        | *0: nothing \| 1: friend \| 2: blocked*                 |


**MAP**

| Field           | Type        | Description                                                                   |
|-----------------|-------------|-------------------------------------------------------------------------------|
| `map_id`          | `int(chron)`  |                                                                               |
| `map_title`       | `string`      | *should be max 200 characters*                                               |
| `map_description` | `string`      |                                                                               |
| `theme`           | `string`      | *integer string depending on the customizations '00' by default can go to something like '66'* |
| `origin_load_x`   | `float: LAT`  |                                                                               |
| `origin_load_y`   | `float: LONG` |                                                                               |
| `marker_count`    | `int`         | *should be limited to 20 markers maybe*                                      |
| `is_deleted`      | `bool`        |                                                                               |

**MAP_USER**

| Field    | Type         | Description                                              |
|----------|--------------|----------------------------------------------------------|
| `map_id`   | `MAP.map_id`   |                                                          |
| `user_id`  | `USER.name`    |                                                          |
| `status`   | `int`          | *0: owner \| 1: collaborator \| 2: spectator*           |

**MARKER**

| Field         | Type          | Description                                              |
|---------------|---------------|----------------------------------------------------------|
| `marker_id`     | `int(chron)`    |                                                          |
| `position_x`    | `float: LAT`    |                                                          |
| `position_y`    | `float: LONG`   |                                                          |
| `translated`    | `string`        | *street address*                                         |
| `map`           | `int: MAP.id`   |                                                          |
| `placer_id`     | `string: USER.name` |                                                      |
| `time_placed`   | `DateTime`      |                                                          |
| `image_count`   | `int`           | *will be capped at 5 images per marker*                 |
| `has_desc`      | `bool`          | *stored as /maps/MAP.map_id/marker_id/image_id*         |
| `is_removed`    | `bool`          |                                                          |

**MAP_REQUEST**

| Field         | Type          | Description                                              |
|---------------|---------------|----------------------------------------------------------|
| `request_id`    | `int(chron)`    |                                                          |
| `sender`        | `USER.name`     |                                                          |
| `receiver`      | `USER.name`     |                                                          |
| `request_type`  | `int`           | *0: collaborator \| 1: spectator*                       |
| `status`        | `int`           | *0: pending \| 1: accepted \| 2: rejected*              |


Using the flowchart and schema ensured SOLID principles and production-ready code 
## 🎥 Website Demos
Here are some demos throughout the process:
https://drive.google.com/drive/folders/1gS8rGF8E800ZelistKDFH2fldJ0onFzv?usp=drive_link

## ❓ Future Features

Some features we wish to implement in the future: 
1. **Profile Management:**
   - Enable users to create and manage their profiles (Location, Interests).
   - Include options for users to add profile pictures and personal information. *
2. **User Interface :**
    - Implement algorithms for directions and routing.
3. **Activity Types:**
   - Define different types of leisure activities (e.g., playing a specific sport, biking, hiking).
   - Let users categorize their shared locations based on activity types. (Leisure, Business) *
4. **Social Features:**
   - Implement a news feed to show updates and activities from following users.
   - Location groups where only users who are in that area can join can be divided into (Province, City, Area) *
   - Chat System *
5. **Notifications:**
   - Send notifications to users for activities such as new location shares, being added to a map, or friend requests.
6. **Rating and Reviews:**
   - Allow users to comment on shared locations.
7. **Reporting and Moderation:**
    - Implement a reporting system for inappropriate content or behaviour.
    - Have a moderation system to review and take action on reported content.* 
