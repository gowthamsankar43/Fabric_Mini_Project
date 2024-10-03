# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# MARKDOWN ********************

# <h1> Requirements Gathering </h1>
# <li>Capacities </li>
# <li>Data Ingestion methods</li> 
# <li>Data Storage options</li>

# MARKDOWN ********************

# <h1> What determines the number of capacities required</h1>
# <ul>
# <li>Compliance with data residency regulations</li>
# <li>Billing preference within the org</li>
# <li>segregating by workload type(DE and BI)</li>
# <li>Segregating by department(finance, marketing, consulting, etc..)</li>
# </ul>
# 
#     

# MARKDOWN ********************

# <h1> What determines the required sizing of a capacity </h1>
# <h2>Intensity of expected workloads</h2>
# <ul>
# <li>High volume of data ingestion</li>
# <li>Heavy transformation(Spark)</li>
# <li>Machine learning training</li>
# </ul>
# <h2>Budget of the workloads</h2>
# <ul>
# <li>Processing time</li>
# <li>F64+ features</li>
# </ul>

# MARKDOWN ********************

# <h1>Data Ingestion Requirements</h1>
<h2>The requirements we need</h2>
<ul>
   <li> The fabric items/features you will need to get data into fabric</li>
   <li> How these items/features will need to be configured</li>
</ul>
<h3> Options to do data ingestion </h3>
<ul>
    <li>Shortcut</li>
    <li>Database mirroring</li>
    <li>ETL - DataFlow </li>
    <li>ETL - DataPipeline </li>
    <li>ETL - Notebook </li>
    <li>ETL - Event Stream </li>
</ul>
<h2> Deciding Factors </h2>
<h3>Where data is stored</h3>
    <ul>  
        <li> ADLSG2, Amazon S3, Google Cloud Storage, Dataverse (ShortCut) </li> 
        <li> Azue SQL, Azure CosmosDB, Snowflake (Database Mirroring)</li>
        <li> On-Premise SQL (ETL-Workflow, ETL-Data Pipeline)</li>
        <li> Realtime events(ETL-Eventstream)</li>
        <li> Others (ETL-Dataflow, ETL-Data Pipeline, ETL-Notebook)</li>
    </ul>
    <h3>What skills exist in the team</h3>
    <ul> 
        <li> Predominantly no/low-code (ETL-Dataflow, ETL-Data Pipeline)</li>
        <li> SQL(ETL-Data Pipeline) </li>
        <li> Spark(Python, Scala, etc)(ETL-Notebook)</li>
    </ul>
    <h3> How is the data Secured?</h3>
    <ul>
        <li> On-premise SQL (On-premise data gateway)</li>
        <li> Azure Virtual Network/Private endpoint (VNet data gateway)</li>
    </ul>
    <h3> What is the volume of the data? </h3>
    <ul> 
        <li> Low (MB's per day)</li>
        <li> Medium(GB's per day)(FastCopy, Staging)</li>
        <li> High(TB's per day)(FastCopy, Staging)</li>
    </ul>



# MARKDOWN ********************

# <h1> Data Storage Requirements </h1>
# <h3> Options for Data storage </h3>
# <ul>
#     <li> Lakehouse </li>
#     <li> Data Warehouse </li>
#     <li> KQL Database </li>
# </ul>
# <h2> Deciding Factors </h2>
# <ul> What is the datatype
#     <li> Structured, Semi-structured, Unstructured (Lakehouse)</li>
#     <li> Relational/Structured (Data Warehouse)</li>
#     <li> Real-time/Streaming (KQL Database)</li>
# </ul>
# <ul> What skills exist in the team
#     <li> T-SQL(Data warehouse)</li>
#     <li> Spark(Python/Spark SQL, Scala)(Lakehouse)</li>
#     <li> KQL(KQL Database)</li>
# </ul>


# MARKDOWN ********************

# %%html
# <h1> Admin Portal </h1>
# <ul> Accessed By Admins
#     <li>Global Administrator</li>
#     <li>Power Platform Administrator</li>
#     <li>Fabric Administrator</li>    
#  </ul>

# MARKDOWN ********************

# <h1> Structure of Fabric Implementation</h1>
# <h4>Tenant &rarr; Capacity &rarr; <b>Workspace &rarr; Item &rarr; Object<b></h4>
# <p> Sharing things in fabric can be done at last three levels</p>
# 
# <h5> Workspace level sharing </h5>
# <p>  </p>
# <p> People or groups can be given workspace-level access.When sharing, the person or goup is assigned a workspace role.
# <li>Admin</li>
# <li>Member</li>
# <li>Contributor</li>
# <li>Viewer</li>
# 
# <p> This role applies to all items in the workspace. For example a Viewer in the workspace will be able to view all items in the workspace</p>
# 
# <h5> Item level sharing</h5>
# <li> Read data</li>
# <li> Read all</li>
# <li> Build reports </li>

