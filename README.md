# Polygon-Partition
Python code for partitioning rectilinear polygon in O(n) time complexity

**<u>Rectillinear Polygon</u> :** A simple connected single-cyclic graph in R<sup>2</sup>, such that each of its edge is perpendicular or in-line with another one of its edge(s). 

*__Method of Labelling the graph__* \
We take input as a rectillinear polygon from cursor keys, i.e., up(↑), left(←), and right (→). As input is read, the pointer proceeds forward and draws a rectillinear polygon with its trail. The labelling of the vertices starts from v<sub>0</sub> to v<sub>n-1</sub>, and v<sub>0</sub> = v<sub>n</sub>, where _n_ is the _number of vertices in the polygon_. 
<br>
<img width="369" alt="pic0" src="https://cloud.githubusercontent.com/assets/10897608/24832576/3ff37ca2-1cd0-11e7-9d87-daf6b46b4dcc.png">

A Rectillinear polygon consisting of 20 vertices.

Pressing a key once means going forward, left, or right. A distance of only one unit can be traversed at a time.

#### INPUTS 
**_G_** = Rectilinear Graph \
**_X_** = Set of Abscissa of vertices \
**_Y_** = Set of Ordinates of vertices \
**_Collinear\_Vertices_** = Set of Collinear Vertices \
**_Concave\_Vertices_** = Set of Concave Vertices \
**_Horizontal\_Chords_** = Set of Horizontal Chords \
**_Vertical\_Chords_** = Set of Vertical Chords

#### Important points to note

    1. Left and Right operations changes the direction the pointer faces.
    2. Vertices that are induced after going forward consecutively. Although in the example, they are not explicitly shown,               but they do exist and at a distance of one unit from its previous vertex.
    3. If the interior angle made by the two edges incident at this vertex is 270 degree.
    4. Chords are lines joining two vertices which are not already part of the polygon.
    5. As, the way of labelling is defined, there is unique labelling of each rectillinear polygon.
    
**EXAMPLE** \
In the above figure, the pointer is shown by an arrow. \
Total number of vertices = 20 \
Collinear\_Vertices = [v<sub>1</sub>, v<sub>2</sub>, v<sub>3</sub>, v<sub>9</sub>, v<sub>13</sub>, v<sub>17</sub>, v<sub>18</sub>, v<sub>19</sub>]
Concave\_Vertices = [v<sub>6</sub>, v<sub>7</sub>, v<sub>12</sub>, v<sub>14</sub>] 

### _**Algorithm for Finding Maximum partitions**_

**Maximum Partition:** Partition of given rectillinear polygon into maximum number of non-overlapping rectangles.

##### STEP I

```python
max_partition(G):
    for u in Concave_Vertices:
        for v in Concave_Vertices and v > u+1:
            if exists a chord joining v & u and ~exists another concave 
             vertex on chord joining v & u:
                if chord is horizontal: 
                    add (v, u) to Horizontal_Chords
                else if chord is vertical:
                    add (v, u) to Vertical_Chords
            else :
                loop_back
```

**_Task Achieved:_** All the edges that exist between *any two concave vertices* are being added to their *respectful categories*. \

**EXAMPLE** \
<img width="371" alt="pic1" src="https://cloud.githubusercontent.com/assets/10897608/24832577/3ffd78b0-1cd0-11e7-90b2-0c13c1642edd.png">

*Horizontal\_Chords* =  ∅ \
*Vertical\_Chords*  =  [(v<sub>7</sub>, v<sub>12</sub>)]

<u>*Explanation*</u>:
**u > v :** Comparison between two vertices is done on the basis of their respective vertex indices. \
Here **_v-u_** should be greater than unity, because this assures the vertex v is not consecutive to u and has a higher index than u. Thus, iteration through each pair of vertex is done only once, making it more efficient. \

In the above code, we iterate through all (concave vertex, concave vertex') pairs, and check for existence of vertical and horizontal chords, that are not intersected by any other vertex. \
We observe that, v<sub>7</sub> and v<sub>12</sub> are the only two concave vertices and between whom, there exists a vertical chord. Therefore, it is added to the set of *Vertical\_Chords*. Also, there does not exist any horizontal chord between any two concave vertices and therefore, set of *Horizontal\_Chords* is empty. \

##### STEP II

```python
    for u in Collinear_Vertices:
        for v in Concave_Vertices:
            if exists a chord joining v & u and ~exists another concave 
                or collinear vertex on chord joining v & u:
                if chord is horizontal:
                    add (v, u) to Horizontal_Chords
                else if chord is vertical:
                    add (v, u) to Vertical_Chords
            else :
                loop_back
```

**_Task Achieved:_** All the chords between *collinear vertices and concave vertices* are being added to their *respective categories*. 

**EXAMPLE** 

<img width="372" alt="pic2" src="https://cloud.githubusercontent.com/assets/10897608/24832578/3fff5aae-1cd0-11e7-9773-45f3f7a7b13e.png">

*Horizontal\_Chords* =  [(v<sub>9</sub>, v<sub>12</sub>), (v<sub>17</sub>, v<sub>14</sub>), (v<sub>18</sub>, v<sub>7</sub>), (v<sub>19</sub>, v<sub>6</sub>)] \
*Vertical_Chords* =  [(v<sub>7</sub>, v<sub>12</sub>), (v<sub>1</sub>, v<sub>4</sub>), (v<sub>3</sub>, v<sub>6</sub>)] 

<u>*Explanation*</u>:
In the above code, we iterate through all (collinear vertex, concave vertex) pairs, and check for existence of vertical and horizontal chords between them, that are not intersected by any other vertex. \
If any chord is found, it is added to set of *Vertical\_Chords* or *Horizontal\_Chords*, depending on its orientation. \

##### STEP III

Thus, we have found all the chords, and only need to plot them now.
```python
    plot(X,Y)
    plot(Horizontal_Chords)
    plot(Vertical_Chords)
    display(plot)
```

<img width="453" alt="test 0 2" src="https://cloud.githubusercontent.com/assets/10897608/24833013/2a39aaca-1cdb-11e7-996a-b8e17434e740.png">

##### STEP IV

Now we have found the maximum partition, but to find the minimum partition the following needs to be done

    1. Find a maximum independent set of chords (i.e., a maximum cardinality set of independent chords).
    2. Draw the chords in this maximum independent set. This partitions the polygon into smaller rectilinear polygons.
    
##### STEP V
From each of the concave vertices from which a chord was not drawn in *Step IV* draw a maximum length vertical line that is wholly within the smaller rectilinear polygon created in *Step III* that contains this vertex.

##### STEP VI

Thus, we have found all the chords, and only need to plot them now.
```python
    plot(X,Y)
    plot(Horizontal_Chords)
    plot(Vertical_Chords)
    plot(Nearest_Partial_Chords)
    display(plot)
```
*Test Case 1*
<img width="1036" alt="test1 1" src="https://cloud.githubusercontent.com/assets/10897608/24833019/2b0da550-1cdb-11e7-9509-3612cd8242de.png">
<img width="436" alt="test 1 2" src="https://cloud.githubusercontent.com/assets/10897608/24833011/2a33018e-1cdb-11e7-8434-c1b139ce9ba6.png">

*Test Case 2*
<img width="946" alt="2 1" src="https://cloud.githubusercontent.com/assets/10897608/24852833/95c4592c-1df6-11e7-8531-70f41ddf4ad5.png">
<img width="434" alt="2 2" src="https://cloud.githubusercontent.com/assets/10897608/24852837/9719ae30-1df6-11e7-860b-69a3e27f8b4f.png">

*Test Case 3*
<img width="1142" alt="3 1" src="https://cloud.githubusercontent.com/assets/10897608/24852836/970f5160-1df6-11e7-915c-20c4c29c541a.png">
<img width="436" alt="3 2" src="https://cloud.githubusercontent.com/assets/10897608/24852834/96ef7426-1df6-11e7-9b7c-004534daa173.png">

*Test Case 4*
<img width="1143" alt="test 4 1" src="https://cloud.githubusercontent.com/assets/10897608/24833014/2a754e7c-1cdb-11e7-8165-e47d3a6e8dc0.png">
<img width="436" alt="test 4 2" src="https://cloud.githubusercontent.com/assets/10897608/24833020/2bf6f584-1cdb-11e7-97fa-5ab28250495b.png">


