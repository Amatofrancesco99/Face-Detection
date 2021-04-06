# Face-Detection
This software is designed to apply artificial intelligence to a real specific application (face-detection).

![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/80333091/113688647-ce612d00-96c9-11eb-8b8e-a4d1728cfbc4.png)

***

*It won't be so difficult to image another application of this software, using a neural network ( in this case a **Cascade Classifier** ) which is trained to recognize other objects, different from the one that whe have chosen in this specific algorithm ( for example: Credit Card, QR Code, Car detection, Pedestrian detection & so on ).*

This would be very easy, by changing some parameters of the source code of this project (made with python).

If you are more interested on last two example, see this project: https://github.com/Amatofrancesco99/Autonomous-Car-Drive ( more specifically the folder: https://github.com/Amatofrancesco99/Autonomous-Car-Drive/tree/main/Detecting%20:%20cars%20%26%20pedestrian )

For the same reason, maybe it would have been better if this repository's title has been something like: *"Object Detection using a Cascade Classifier"*, but the aim of this project would have been less easier to understand (maybe too general, also if, as known, a software is not designed to solve a specific problem but for a general purpose solution to a group of problems ). 

**P.S:** Don't take this software as a "must"...it's a rudimental script to better understand how facial recognition works ( and how easy it can be implemented ). 
You all are free to use this code and add new useful features... I'll be glad if this project could bring benefits just only for one of you.
I'll then try to explain each line of the code, as better as I can, with a few comments. 

***

The algorithm implements a *Cascade Classifier*, more specifically **Haar Classifier for Object Detection** ( based on brightness characteristic of every human face; it uses only black-white images to do what I said before ) . 

If you are more interested to see how this specific Classifier works, there's an **useful link**: 
   - https://www.sciencedirect.com/topics/computer-science/classifier-cascade

**VIDEO: *HOW HAAR CASCADE WORKS***

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/hPCTwxF0qf4/0.jpg)](https://www.youtube.com/watch?v=hPCTwxF0qf4)

***

Maybe this algorithm won't be 100% accurate (there's a little margin of error), but it is very fast, simple both to code ( just few lines of code ) both to understand. 

In lot cases whe should have a trade-off/compromise between two or more issues ( in this case speed vs accuracy vs semplicity... the more the software is accurate, the less "fluent" & the more complex it would be ).
