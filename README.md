# MongoDB_Python
Basic python script to connect with MongoDB Atlas (Cloud based MongoDb) to perform basic CRUD operations, like creating collection in mongoDB database, then inserting, retrieving, updating and deleting documents (data) in collections


### What is MongoDB?

MongoDB is a well-known open-source NoSQL database built on the C++ programming language. MongoDB is a document-oriented database that uses JSON-like documents and a Dynamic Schema to store information. It means that while saving your data, you won’t have to worry about the Data Structure, the number of fields or the types of fields used to store values. JSON objects are identical to MongoDB Documents.

You can change the structure of records by simply adding new fields or deleting existing ones (which MongoDB refers to as Documents). This functionality can be used to describe Hierarchical Relationships, Store Arrays, and other more sophisticated Data Structures in MongoDB. MongoDB is being utilized to store enormous volumes of data by a number of digital companies, including Facebook, eBay, Adobe, and Google.

### Key Features of MongoDB
In comparison to other traditional databases, MongoDB has a number of unique features that make it a superior choice. The following are some of these attributes:

* Index-based Document: In a MongoDB database, every field in the Document is indexed with Primary and Secondary Indices, making it easier to get data from the pool.
* Horizontal Scalability: It is possible with MongoDB’s sharding. The practice of distributing data over numerous servers is known as sharding. The Shard Key is used to partition a huge quantity of data into data chunks, which are then uniformly dispersed among Shards that span several Physical Servers.
* Schema-Less Database: This type of Database stores many sorts of documents in a single collection (the equivalent of a table). To put it another way, a single collection in the MongoDB database can hold numerous documents, each having its own set of Fields, Content, and Size. It is not required that one document be comparable to another, as it is with Relational Databases. MongoDB provides a lot of freedom to consumers because of this capability.
* Replication: MongoDB provides high availability of data by generating several copies of the data and sending these copies to a separate Server, allowing the data to be retrieved even if one server fails

### Installing MongoDB
To start with Windows MongoDB Shell installation you need to have MongoDB installed in the first place. If you don’t already have MongoDB installed on your computer, the first section will put you through just before moving on to the installation of the MongoDB shell. You can skip this section if you have already installed MongoDB on your system.

Before installing MongoDB, it is important to know that there are 2 editions: Community Edition and the Enterprise Edition. The major difference between the Community edition(regular enough for developers) and the Enterprise edition is that it provides advanced security options(e.g LDAP, auditing, log redaction), additional storage engines, real-time server stats, document validation, MongoDB connector for BI, schema analysis and many more. 

#### Download The Installer
* Go to the download page at https://www.mongodb.com/try/download/community
* Choose your OS and your desired MongoDB version.
* Click Download.
#### You can also use MongoDB Atlas which is cloud based MongoDB.
Link: https://rb.gy/9nbn3a
