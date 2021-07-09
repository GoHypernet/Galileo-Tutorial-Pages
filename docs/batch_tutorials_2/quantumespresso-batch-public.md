# Tutorial: Running Quantum Espresso in Galileo

### Gettting started with Quantum Espresso in Galileo

To get started with Galileo, [log into your account](http://galileo.hypernetlabs.io/) using Firefox or Chrome.

### Understanding the user interface and cloning a Mission

When you log into Galileo, the first thing you’ll see is your Dashboard:

![View of the Galileo Dashboard](images/common/dashboard.png)

To run the Quantum Espresso example, start by navigating to the Missions tab using the side menu. Clone the Quantum Espresso example Mission from the Explore Missions tab. Use the filter to search for the mission by name and click "Apply".

![Find the public example mission by name](images/quantumespresso/find_public.png)

Once you have found the correct Mission, click "View Mission".

![Click View Mission](images/quantumespresso/example_mission.png)

To clone the public Mission to your account, click the "Clone" button in the upper right corner of the interface. Choose between creating a public or private clone and also choose which Cargo Bay to use.

![Clone the mission](images/quantumespresso/clone_mission.png)

You will now see a cloned copy of the Mission in your Missions.

![The cloned copy](images/quantumespresso/cloned_copy.png)

### Let's take a look at our files

First, we have a series of files to run our computations: `pw.methane.in` is an input file that conducts the SCF ground-state calculation, `turbo_davidson.methane.in` runs a Davidson calculation of our eigenvalues, and `turbo_spectrum.methane.in` completes a post-processing analysis of our spectrum.

We also have the files `plot_spectrum_nohyb.gp` and `plot_spectrum_hyb.gp`, which plot our spectrum using gnuplot with and without B3LYP pseudo-potential, respectively.

Finally, we have a shell script called `runqe.sh` that contains our QE commands.

### Running a job and collecting results

Now we are ready to run a job using the Mission. Click the **Run** button in the upper right corner of the Mission tab. You will see a "Mission run successfully!" message. At the bottom of the Mission tab, you can track the progress of the job.

![Track job progress](images/quantumespresso/track_job.png)

Once the computation is completed, the job will shut down and collect the results. Once the job progress reads "Completed", you can download the results by opening the three-dot menu and clicking **Download**.

![Download results](images/quantumespresso/download.png)

Let's take a look at the output log:

![Results](images/quantumespresso/results.png)

### Contact us

We hope this tutorial was helpful. Please let us know if you have any questions or any problems using Galileo. Your feedback is extremely important to us. Contact us anytime at [matthew@hypernetlabs.io](matthew@hypernetlabs.io) or [alexander@hypernetlabs.io](alexander@hypernetlabs.io).