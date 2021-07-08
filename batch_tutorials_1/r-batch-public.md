# Tutorial: Running R in Galileo

### Gettting started with R in Galileo

To get started with Galileo, [log into your account](http://galileo.hypernetlabs.io/) using Firefox or Chrome.

### Understanding the user interface and cloning a Mission

When you log into Galileo, the first thing you’ll see is your Dashboard:

![View of the Galileo Dashboard](images/common/dashboard.png)

To run the R example, start by navigating to the Missions tab using the side menu. Clone the R Batch example Mission from the Explore Missions tab. Use the filter to search for the mission by name and click "Apply".

![Find the public example mission by name](images/r/find_public.png)

Once you have found the correct Mission, click "View Mission".

![Click View Mission](images/r/example_mission.png)

To clone the public Mission to your account, click the "Clone" button in the upper right corner of the interface. Choose between creating a public or private clone and also choose which Cargo Bay to use.

![Clone the mission](images/r/clone_mission.png)

You will now see a cloned copy of the Mission in your Missions.

![The cloned copy](images/r/cloned_copy.png)

### Let's take a look at our files

The rMonteCarlo.R script conducts a linear regression, makes a simple plot, and then runs two Monte Carlo simulations.

The first Monte Carlo simulates tossing two dice and calculates the number of rolls that are 7 or less. The second Monte Carlo increases the number of iterations and runs the simulation in parallel.

### Running a job and collecting results

Now we are ready to run a job using the Mission. Click the **Run** button in the upper right corner of the Mission tab. You will see a "Mission run successfully!" message. At the bottom of the Mission tab, you can track the progress of the job.

![Track job progress](images/r/track_job.png)

Once the computation is completed, the job will shut down and collect the results. Once the job progress reads "Completed", you can download the results by opening the three-dot menu and clicking **Download**.

![Download results](images/r/download.png)

Let's take a look at the the output.log file first, which returns the results of the regression and simulation:

![Output.log results](images/r/results.png)

Next, if we look in the results folder, we can see the plot we created for the regression:

![Regression plot](images/r/regression_fit.jpg)

### Contact us

We hope this tutorial was helpful. Please let us know if you have any questions or any problems using Galileo. Your feedback is extremely important to us. Contact us anytime at [matthew@hypernetlabs.io](matthew@hypernetlabs.io) or [alexander@hypernetlabs.io](alexander@hypernetlabs.io).