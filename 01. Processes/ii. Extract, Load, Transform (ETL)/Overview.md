# Extract, Transform, Load (ETL)

The [ETL (Extract, Transform, Load)](https://aws.amazon.com/what-is/etl/) process is a data integration approach, and in the context of AWS or cloud computing in general, services like AWS Glue are commonly used for ETL tasks. ETL is like a data movement and transformation choreographer, handling the flow of information from various sources to a destination where it can be analyzed or utilized.

- Firstly, in the "Extract" phase, data is gathered from different sources—this could be databases, logs, or other data repositories. AWS Glue simplifies this step by automatically discovering and extracting data from various sources.
- Next comes the "Transform" phase, where the extracted data is cleaned, filtered, and transformed into a format suitable for analysis or storage. AWS Glue provides tools to define these transformations without requiring deep technical expertise, making it accessible to a broader audience.
- Lastly, in the "Load" phase, the transformed data is loaded into a destination, typically a data warehouse, database, or data lake. AWS Glue automates this loading process, ensuring that the data ends up where it needs to be efficiently.

Key benefits include scalability (handling both small and large datasets), automation (reducing manual effort), and the ability to schedule and monitor ETL jobs. This process is fundamental for organizations aiming to derive insights from their data or consolidate information from various sources into a centralized repository for analysis.

# Pulsar Use Case

``` mermaid
%% GRAPH DESIGN
flowchart LR
raw --> glue --- catalog --- crawler --> curated

%% COMPONENTS
raw[(S3 Raw)]
glue[AWS Glue]
catalog[AWS Glue Data Catalog]
crawler[AWS Crawler]
curated[(S3 Curated)]

%% STYLING
style raw fill:#E05243
style curated fill:#E05243
style glue fill:#6737C4
style catalog fill:#6737C4
style crawler fill:#6737C4

```