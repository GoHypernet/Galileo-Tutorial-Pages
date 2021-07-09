# Tutorial: Running MAFFT in Galileo

### Getting started with MAFFT in Galileo

To get started with Galileo, [log into your account](http://galileo.hypernetlabs.io/) using Firefox or Chrome.

### Understanding the user interface and cloning a Mission

When you log into Galileo, the first thing you’ll see is your Dashboard:

![View of the Galileo Dashboard](images/common/dashboard.png)

To run the MAFFT example, start by navigating to the Missions tab using the side menu. Clone the MAFFT example Mission from the Explore Missions tab. Use the filter to search for the mission by name and click "Apply".

![Find the public example mission by name](images/mafft/find_public.png)

Once you have found the correct Mission, click "View Mission".

![Click View Mission](images/mafft/example_mission.png)

To clone the public Mission to your account, click the "Clone" button in the upper right corner of the interface. Choose between creating a public or private clone and also choose which Cargo Bay to use.

![Clone the mission](images/mafft/clone_mission.png)

You will now see a cloned copy of the Mission in your Missions.

![The cloned copy](images/mafft/cloned_copy.png)

### Let's take a look at our files

This tutorial demonstrates how to use MAFFT. MAFFT creates multiple sequence alignments (MSA) of nucleotides or protein sequences (genomes) and aligns all the sequences together and visualizes how they differ:

![Multiple sequence alignment of 18 protein sequences](images/mafft/protein.png)

In our example folder, we have the file, “input.fasta”. The MAFFT program takes as input a file of genome or protein sequences in a format called “FASTA”, hence the “input.fasta”. This file format is commonly used in bioinformatics.

### Running a job and collecting results

Now we are ready to run a job using the Mission. Click the **Run** button in the upper right corner of the Mission tab. You will see a "Mission run successfully!" message. At the bottom of the Mission tab, you can track the progress of the job.

![Track job progress](images/mafft/track_job.png)

Once the computation is completed, the job will shut down and collect the results. Once the job progress reads "Completed", you can download the results by opening the three-dot menu and clicking **Download**.

![Download results](images/mafft/download.png)

Let's take a look at the results.fasta:

![Results](images/mafft/results.png)

### Contact us

We hope this tutorial was helpful. Please let us know if you have any questions or any problems using Galileo. Your feedback is extremely important to us. Contact us anytime at [matthew@hypernetlabs.io](matthew@hypernetlabs.io) or [alexander@hypernetlabs.io](alexander@hypernetlabs.io).