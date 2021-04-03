# Facial-Recognition
This software is designed to apply artificial intelligence to a real specific application (facial-recognition).

***

*It won't be so difficult to image another application of this software, using a neural network ( in this case a **Cascade Classifier** ) which is trained to recognize other objects, different from the one that whe have chosen in this specific algorithm ( for example: Credit Card, QR Code, Car detection, Pedestrian detection & so on ).*

This would be very easy, you just have to change some parameters of the source code of this project (made with python).

For the same reason, maybe it would have been better if this repository's title has been something like: *"Object Detection using a Cascade Classifier"*, but the aim of this project would have been less easier to understand (maybe too general, also if, as known, a software is not designed to solve a specific problem but for a general purpose solution to a group of problems ). 

**P.S:** Don't take this software as a "must"...it's a rudimental script to better understand how facial recognition works ( and how easy it can be implemented ). 
You all are free to use this code and add new useful features... I'll be glad if this project could bring benefits just only for one of you.
I'll then try to explain each line of the code, as better as I can, with a few comments. 

***

The algorithm implements a *Cascade Classifier*, more specifically **Haar Classifier for Object Detection** ( based on brightness characteristic of every human face; it uses only black-white images to do what I said before ) . 

If you are more interested to see how this specific Classifier works, there's a **useful link**: 
   - https://www.sciencedirect.com/topics/computer-science/classifier-cascade )

***

Maybe this algorithm won't be so accurate, but it is very fast, simple both to code ( just few lines of code ) both to understand. 

In lot cases whe should have a trade-off/compromise between two or more issues ( in this case speed vs accuracy vs semplicity... the more the software is accurate, the less "fluent" & the more complex it would be ).
