Future forge team – WRO future engineers 2026
![Banner](Images/banner.jpg)
---
Table of contents
About us
Power and sense management
Obstacle management
Engineering factor
Hardware
Software
Experience and acquired expertise
Special thanks
Conclusion and future vision
<br>
About us
We are a team of two members:

Amr Younis
A fifteen-year-old Palestinian.  
Instagram: amr.younis04<br>

Mohammad Younis
A fourteen-year-old Palestinian.  
Instagram: *******<br>

We are pleased to introduce our project, which involves building and programming a robot capable of traversing a specific path. This path consists of a white carpet with two lines in each corner, as well as an orange line and a blue line. The carpet measures three meters long and three meters wide, surrounded by a 10-cm-high black wooden wall, with a 10-cm-high square black wooden wall in the middle of the carpet.<br>
<br>
Power and sense management
We used a 12.6-volt, 6A rechargeable lithium battery. It’s a medium-weight battery with large capacity, sufficient for all components. We distributed the power correctly so that no single component consumes more than its share.<br>
<br>
Obstacle management
The robot deals with obstacles using ultrasonic sensors and a camera.
Ultrasonic technology measures the distance between the obstacle and the robot, enabling it to adjust its direction. It works by sending out sound waves and measuring their bounce.
The camera recognizes colors and sends a signal to the Raspberry Pi. For example, when detecting red, the robot reacts according to the instructions we programmed.<br>
<br>
Engineering factor
We started with a ready-made kit and modified it to suit our task. For example, we added additional layers to contain all the parts and ensured balanced weight distribution, placing the battery in the middle to prevent tilting.<br>

<hr>
<h1 id="hardware" style="font-family:Verdana; color:blue;">Hardware</h1>
<h2 style="font-family:Verdana; color:blue;">1- The robot</h2>
<div style="overflow:hidden;">
  <p style="font-family:Verdana; float:left; width:60%;">
    We modified a ready-made kit by adding one acrylic layer and two plastic layers, giving us four in total:
    <ul style="font-family:Verdana;">
      <li>Ground layer: DC motor and servo motor</li>
      <li>Second layer: battery</li>
      <li>Third layer: power button and power regulation circuit</li>
      <li>Fourth layer: Raspberry Pi, gyroscope, three ultrasonic sensors, camera and motor driver</li>
    </ul>
    All connected with jumper wires.
  </p>
<img src="Images/Robot.jpg" alt="Robot" width="250" style="float:right; margin-left:15px;">
</div>
<!-- الصور على اليمين -->
<h2 style="font-family:Verdana; color:blue;">2- Kit used</h2>
<p style="font-family:Verdana;">
MG996 car model servo and DC motor<br>
Available in Palestine and suitable for our task<br>
</p>
<p style="font-family:Verdana;">
<img src="Images/Kit.jpg" alt="Robot Kit" width="250" style="float:right; margin-left:15px;">
</p>
<h2 style="font-family:Verdana; color:blue;">3- Microcontroller</h2>
<p style="font-family:Verdana;">
Raspberry Pi 4 8GB RAM<br>
Fast CPU, Python support, and available locally<br>
Cost: $92 for 1pcs <a href="https://ar.aliexpress.com/item/1005012191207911.html?spm=a2g0o.detail.pcDetailTopMoreOtherSeller.2.418331ps31psFq&gps-id=pcDetailTopMoreOtherSeller&scm=1007.40050.354490.0&scm_id=1007.40050.354490.0&scm-url=1007.40050.354490.0&pvid=59b22c2f-3eac-463d-aa44-a9f8a4eb72b5&_t=gps-id%3ApcDetailTopMoreOtherSeller%2Cscm-url%3A1007.40050.354490.0%2Cpvid%3A59b22c2f-3eac-463d-aa44-a9f8a4eb72b5%2Ctpp_buckets%3A668%232846%238108%231977&pdp_ext_f=%7B%22order%22%3A%223%22%2C%22eval%22%3A%221%22%2C%22sceneId%22%3A%2230050%22%2C%22fromPage%22%3A%22recommend%22%7D&pdp_npi=6%40dis%21USD%21119.69%21119.69%21%21%21806.00%21806.00%21%4021016b6017847426850993529e1e04%2112000057721429210%21rec%21PS%21%21ABXZ%211%210%21n_tag%3A-29910%3Bd%3Aa7b94305%3Bm03_new_user%3A-29895&utparam-url=scene%3ApcDetailTopMoreOtherSeller%7Cquery_from%3A%7Cx_object_id%3A1005012191207911%7C_p_origin_prod%3A" target="_blank">AliExpress</a>
</p>
<img src="Images/RaspberryPi.jpg" alt="Battery" width="250">
<h2 style="font-family:Verdana; color:blue;">4- Battery</h2>
<p style="font-family:Verdana;">
    12.6V, 6A lithium battery<br>
    High voltage & capacity, adjustable output<br>
    Cost: $16.56 for battery and charger - 
    <a href="https://ar.aliexpress.com/item/1005009355610829.html?invitationCode=RUkva01yN3FrcHorcEtMRk5pZm9YS20zcVMyeFBybGRsclFQNndUbXRSND0&srcSns=sns_Copy&spreadType=socialShare&social_params=6000468078908&bizType=ProductDetail&spreadCode=RUkva01yN3FrcHorcEtMRk5pZm9YS20zcVMyeFBybGRsclFQNndUbXRSND0&aff_fcid=bf1012543d994825af7cc2b2e55e3460-1784742163089-01161-_c2yQB6m7&tt=MG&aff_fsk=_c2yQB6m7&aff_platform=default&sk=_c2yQB6m7&aff_trace_key=bf1012543d994825af7cc2b2e55e3460-1784742163089-01161-_c2yQB6m7&shareId=6000468078908&businessType=ProductDetail&platform=AE&terminal_id=440e1d6f404e4fbb83abc7e7edd8131f&afSmartRedirect=y" target="_blank">AliExpress</a>
</p>
<img src="Images/Battery.jpg" alt="Battery" width="250">
<h2 style="font-family:Verdana; color:blue;">5- DC power converter</h2>
<p style="font-family:Verdana;">
XL4015 (32V → 1.25V adjustable)<br>
Easy to install<br>
Cost: $0.59 for 1pcs <a href="https://ar.aliexpress.com/item/1005007993082705.html?spm=a2g0o.productlist.main.6.392bjz58jz58tC&algo_pvid=29329bb0-8f20-4438-a348-4aebff5423bb&algo_exp_id=29329bb0-8f20-4438-a348-4aebff5423bb-5&pdp_ext_f=%7B%22order%22%3A%22905%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%210.80%210.59%21%21%210.80%210.59%21%402141147417847413344477799e1c51%2112000043188785128%21sea%21PS%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Aa7b94305%3Bm03_new_user%3A-29895&curPageLogUid=WHaQ7XyJFLTo&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005007993082705%7C_p_origin_prod%3A" target="_blank">AliExpress</a>
</p>
<img src="Images/Converter.jpg" alt="DC Converter" width="250">
<h2 style="font-family:Verdana; color:blue;">6- Ultrasonic sensors</h2>
<p style="font-family:Verdana;">
3 × HC-SR04<br>
Voltage: 3.3 to 5V<br>
Range: 2cm to 400cm<br>
Cost: $0.96 for 1 pcs <a href="https://ar.aliexpress.com/item/1005009463448139.html?spm=a2g0o.productlist.main.7.3d62BlExBlExjR&algo_pvid=72d04225-bab3-4c2b-87e3-7cf3acc3eb82&algo_exp_id=72d04225-bab3-4c2b-87e3-7cf3acc3eb82-6&pdp_ext_f=%7B%22order%22%3A%225%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%211.20%210.96%21%21%211.20%210.96%21%402101737817847411970475388e1d5b%2112000049183289560%21sea%21PS%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Aa7b94305%3Bm03_new_user%3A-29895&curPageLogUid=3RExpklPMQbS&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009463448139%7C_p_origin_prod%3A" target="_blank">AliExpress</a>
</p>
<img src="Images/Ultrasonic.jpg" alt="Ultrasonic Sensor" width="250">
<h2 style="font-family:Verdana; color:blue;">7- Motor driver</h2>
<p style="font-family:Verdana;">
L298N motor driver<br>
Sufficient for our motors<br>
Cost: $1.23 for 1 pcs <a href="https://ar.aliexpress.com/item/1005009009975262.html?spm=a2g0o.detail.pcDetailTopMoreOtherSeller.1.746a2zgH2zgHYH&gps-id=pcDetailTopMoreOtherSeller&scm=1007.40050.354490.0&scm_id=1007.40050.354490.0&scm-url=1007.40050.354490.0&pvid=589a13cd-90f9-438d-8c22-7eeb194658c1&_t=gps-id%3ApcDetailTopMoreOtherSeller%2Cscm-url%3A1007.40050.354490.0%2Cpvid%3A589a13cd-90f9-438d-8c22-7eeb194658c1%2Ctpp_buckets%3A668%232846%238109%231935&pdp_ext_f=%7B%22order%22%3A%22101%22%2C%22spu_best_type%22%3A%22price%22%2C%22eval%22%3A%221%22%2C%22sceneId%22%3A%2230050%22%2C%22fromPage%22%3A%22recommend%22%7D&pdp_npi=6%40dis%21USD%212.73%211.23%21%21%2118.40%218.28%21%400be71e1e17847410011543797e1864%2112000047569477477%21rec%21PS%21%21ABX%211%210%21n_tag%3A-29910%3Bd%3Aa7b94305%3Bm03_new_user%3A-29895&utparam-url=scene%3ApcDetailTopMoreOtherSeller%7Cquery_from%3A%7Cx_object_id%3A1005009009975262%7C_p_origin_prod%3A" target="_blank">AliExpress</a>
</p>
<img src="Images/MotorDriver.jpg" alt="Motor Driver" width="250">
<h2 style="font-family:Verdana; color:blue;">8- Gyroscope</h2>
<p style="font-family:Verdana;">
MPU-6050 gyroscope and accelerometer<br>
Small, efficient, available<br>
Cost: $0.88 for 1 pcs <a href="https://ar.aliexpress.com/item/1005012328759231.html?spm=a2g0o.detail.pcDetailTopMoreOtherSeller.3.2b7a3Use3UsefC&gps-id=pcDetailTopMoreOtherSeller&scm=1007.40050.354490.0&scm_id=1007.40050.354490.0&scm-url=1007.40050.354490.0&pvid=e7519f90-73f4-4ba4-9fb7-0f40e32e66b2&_t=gps-id%3ApcDetailTopMoreOtherSeller%2Cscm-url%3A1007.40050.354490.0%2Cpvid%3Ae7519f90-73f4-4ba4-9fb7-0f40e32e66b2%2Ctpp_buckets%3A668%232846%238116%232002&pdp_ext_f=%7B%22order%22%3A%226%22%2C%22eval%22%3A%221%22%2C%22sceneId%22%3A%2230050%22%2C%22fromPage%22%3A%22recommend%22%7D&pdp_npi=6%40dis%21USD%211.26%210.88%21%21%218.50%215.95%21%40214134eb17847407379828759e0f88%2112000058093179730%21rec%21PS%21%21ABX%211%210%21n_tag%3A-29910%3Bd%3Aa7b94305%3Bm03_new_user%3A-29895&utparam-url=scene%3ApcDetailTopMoreOtherSeller%7Cquery_from%3A%7Cx_object_id%3A1005012328759231%7C_p_origin_prod%3A" target="_blank">AliExpress</a>
</p>
<img src="Images/Gyroscope.jpg" alt="Gyroscope" width="250">
<h2 style="font-family:Verdana; color:blue;">9- Camera</h2>
<p style="font-family:Verdana;">
    Ultra-wide USB camera<br>
    Better than Pi camera & easier to program<br>
    Cost: $8.42 for 1 pcs - 
    <a href="https://ar.aliexpress.com/item/1005006310117710.html?spm=a2g0o.productlist.main.6.2873FeiGFeiGQo&algo_pvid=6e5bf61f-f223-4bb8-9a9f-78cd9e7f9999&algo_exp_id=6e5bf61f-f223-4bb8-9a9f-78cd9e7f9999-5&pdp_ext_f=%7B%22order%22%3A%2248%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%2115.59%218.42%21%21%21105.00%2156.70%21%40212a6dc917847403641025824e1d16%2112000036710580625%21sea%21PS%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Aa7b94305%3Bm03_new_user%3A-29895&curPageLogUid=fB3HsKUFge0w&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005006310117710%7C_p_origin_prod%3A" target="_blank">AliExpress</a>
</p>
<img src="Images/Camera.jpg" alt="Camera" width="250">
<h2 style="font-family:Verdana; color:blue;">10- Jumper wires</h2>
<p style="font-family:Verdana;">
Male to male, male to female, female to female<br>
Strong, reusable, Raspberry Pi compatible<br>
Cost: $0.61 for 40 pcs  <a href="https://ar.aliexpress.com/item/1005010322998753.html?spm=a2g0o.detail.pcDetailBottomMoreOtherSeller.4.7b3ceWYxeWYxlo&gps-id=pcDetailBottomMoreOtherSeller&scm=1007.40050.354490.0&scm_id=1007.40050.354490.0&scm-url=1007.40050.354490.0&pvid=3e3b0bb1-dfc1-467d-a377-43f95fcc9c79&_t=gps-id%3ApcDetailBottomMoreOtherSeller%2Cscm-url%3A1007.40050.354490.0%2Cpvid%3A3e3b0bb1-dfc1-467d-a377-43f95fcc9c79&pdp_ext_f=%7B%22order%22%3A%22203%22%2C%22eval%22%3A%221%22%2C%22sceneId%22%3A%2230050%22%2C%22fromPage%22%3A%22recommend%22%7D&pdp_npi=6%40dis%21USD%211.07%210.54%21%21%217.19%213.59%21%402141147417847393053923158e1b8b%2112000051952266061%21rec%21PS%21%21ABX%211%210%21n_tag%3A-29910%3Bd%3Aa7b94305%3Bm03_new_user%3A-29895&utparam-url=scene%3ApcDetailBottomMoreOtherSeller%7Cquery_from%3A%7Cx_object_id%3A1005010322998753%7C_p_origin_prod%3A" target="_blank">AliExpress</a>
</p>
<img src="Images/JumperWires.jpg" alt="Jumper Wires" width="250">
<h2 style="font-family:Verdana; color:blue;">11- On/off button</h2>
<p style="font-family:Verdana;">
Regular on/off switch<br>
Inexpensive and easy to install<br>
Cost: $0.67 for two pcs <a href="https://ar.aliexpress.com/item/1005009187497448.html?spm=a2g0o.productlist.main.4.6659VBZPVBZPji&algo_pvid=cde2e5a6-6cc3-4bcb-95f0-911d00f2b081&aem_p4p_detail=2026072209473612241155076612200000032710&algo_exp_id=cde2e5a6-6cc3-4bcb-95f0-911d00f2b081-3&pdp_ext_f=%7B%22order%22%3A%22347%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%214.50%213.15%21%21%214.50%213.15%21%4021413b0b17847388566187049e1053%2112000048235993795%21sea%21PS%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Aa7b94305%3Bm03_new_user%3A-29895&curPageLogUid=ml6vri059rQj&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005009187497448%7C_p_origin_prod%3A&search_p4p_id=2026072209473612241155076612200000032710_1" target="_blank">AliExpress</a>
</p>
<img src="Images/OnOffButton.jpg" alt="On/Off Button" width="250">
---
Software
We programmed the robot using Python 3 on Linux (Raspberry Pi OS). Python was chosen for its large library support and flexibility. Libraries such as OpenCV were used for image processing, while GPIO libraries allowed us to control motors and sensors.
---
Experience and acquired expertise
This project gave us valuable skills:
Teamwork and decision-making
Problem-solving in programming and hardware
Overcoming obstacles in robotics for the first time
We also gained technical expertise:
Computer vision and sensor integration
Open-source robotics design
Balancing power, weight, and stability in engineering design
---
Conclusion and future vision
This project was not just about building a robot — it was about proving what motivated students can achieve with creativity, persistence, and teamwork.
Our next steps will focus on turning our passion for robotics into solutions that can help people in everyday life. From intelligent navigation systems to practical automation, we aim to expand the boundaries of what we can design and build.
Future forge team – building today, imagining tomorrow
