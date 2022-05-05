# Automated Solar Tracking System
This repository hosts the codebase for the Automated Solar Tracking System 2022 senior project at Missouri University of Science and Technology (Missouri S&T).


Group Members
Matt Bowie, Electrical Engineering - Team Lead/Software Engineer
Jeremy Long, Electrical Engineering - Software Engineer/Hardware Design
Bronson Tavenner, Electrical Engineering - Physical design and construction
Aaron Ivie, Electrical Engineering - Physical design and construction

Technical Advisor
Dr. Tayo Obafemi-Ajayi - Professor of Electrical Engineering, Missouri S&T/Missouri State University

Special Thanks
Dr. Doug Carroll - Director, Missouri S&T/Missouri State University Cooperative Engineering Program

Project Presentation: https://youtu.be/HawqlIfnLps

Abstract
Due to the increasing world population and the depletion of many natural resources, there is a larger need for renewable energy than ever before. Solar energy is a popular alternative to the burning of fossil fuels due to its near infinitely renewable nature. As better technology develops, solar energy can become the best source of renewable energy. The goal of this project was to design an automated solar tracking system that follows the sun as it moves through the sky, increasing the efficiency of energy production when compared to a stationary solar panel. A Raspberry Pi Zero is being used as the system controller. It handles the calculations for the sun’s location via a mathematical model, driving of the two axis motors, and processing of the data collected by the power sensor. To start the program the user will need to insert a flash drive with the coordinates of their current location and flip three switches on the front panel. Once that has been done, the system runs itself with no need for human interface. The system consists of two motors that allow the solar panel to twist and tilt to track the sun based on the mathematical model. The declination angle, latitude, longitude, and hour angle are all factors that play a role into the mathematical model of the sun. The efficiency of a tracking system could greatly impact the future of renewable energy sources.
