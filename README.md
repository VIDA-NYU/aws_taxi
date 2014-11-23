NYC Taxi Analysis
========

Sample scripts to analyze taxi data on Amazon AWS

Instruction
-----------

1. Create an Amazon EMR cluster with the following configuration (the bootstrap action is very important -- please pay attention to that):

        * Termination protection: Yes
        * Logging: Enabled (remember to input your S3 bucket to store log file)
        * Hadoop distribution: Amazon AMI 3.3.1
        * Bootstrap action: This is a very important step because the sample scripts 
        make use of python rtree library, but Amazon AMI 3.3.1 does not have rtree installed.
        Click 'Add bootstrap action' -> Custom action -> Configure and add -> 
        Put the following in 'S3 location': s3://mda2014/rtree.sh
        * Don't add any step at this point
        * Cluster Auto-terminate: No

2. Clone this repository and upload the neighborhoods and yearplot scripts to your bucket on S3. For example:

        * neighborhoods: s3://mda2014/neighborhoods
        * yearplot: s3://mda2014/yearplot
        
3. To run neighborhoods script: Add the following streaming step to your cluster with the following information:

        Replace mda2014 with your bucket name, except in Input
        * Mapper: s3://mda2014/neighborhoods/mapper.py
        * Reducer: s3://mda2014/neighborhoods/reducer.py
        * Input: s3://mda2014/taxi/trip/
        * Output: s3://mda2014/output1
        * Arguments: -files s3://mda2014/neighborhoods/mapper.py,s3://mda2014/neighborhoods/reducer.py,s3://mda2014/neighborhoods/shapefile.py,s3://mda2014/neighborhoods/ZillowNeighborhoods-NY.shp,s3://mda2014/neighborhoods/ZillowNeighborhoods-NY.prj,s3://mda2014/neighborhoods/ZillowNeighborhoods-NY.shp.xml,s3://mda2014/neighborhoods/ZillowNeighborhoods-NY.shx,s3://mda2014/neighborhoods/ZillowNeighborhoods-NY.dbf
        
    Wait for finish, then download and merge all output into one file called `output.txt`

    To generate plot, execute:

        python plot_results.py output.txt <location_of_output_plot>

4. To run yearplot script: Add the following streaming step to your cluster with the following information:

        Replace mda2014 with your bucket name, except in Input
        * Mapper: s3://mda2014/yearplot/mapper.py
        * Reducer: s3://mda2014/yearplot/reducer.py
        * Input: s3://mda2014/taxi/trip/
        * Output: s3://mda2014/output2

    Wait for finish, then download and merge all output into one file called `output.txt`

    To generate plot, execute:

        python plot_results.py output.txt <location_of_output_plot>
              
5. Remember to terminate cluster after use.

Author
======

[Huy T. Vo](http://serv.cusp.nyu.edu/~hvo/)


Contributors
============

[Tuan-Anh Hoang-Vu](http://bigdata.poly.edu/~tuananh/)
