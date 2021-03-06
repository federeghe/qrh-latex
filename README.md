# qrh-latex
Quick Reference Handbook package for LaTeX.

Quick Reference Handbooks or QRHs are specific manuals used by pilots. A QRH contains all normal and abnormal procedures for flying a specific
aircraft. A more detailed definition can be found [at skybrary](http://www.skybrary.aero/index.php/Quick_Reference_Handbook).

How to build package
--------------------
sty files are already built. However, you can exec `make` and `make install` under package directory to install to your system the package. *Do not use qty-helper package*, it's an include file for main package `qty`.

You should check and edit Makefile to set the correct values for compilers and destination directory.

How to build your checklist
---------------------------
After write your checklist, you need to create the `.toc` file before build it. Currently LaTeX implementation doesn't create the `.toc` file, so you need to execute the tool presents under tools directory (python >= 3.1 required).

Exposed commands reference
--------------------------

You should separate each page with `\newpage` and set as first the `\QRHheading` (explained below). You should not split the checklist in more pages.

This package contains the following commands:
* `\QRHfirstpage`: the front page of the document. It has 4 parameters: an image path, aircraft full name, aircraft short name (A320, B737, P180, etc.), and revision number.
* `\QRHheading`: it is the header of each page. It has no parameters,
* `\QRHbody`: it is the body of each checklist. If checklists are short you can put them in the same page, but remember: never split a checklist over
two pages! (Also this is never done in real aviation QRH). It accepts 2 parameters: checklist name, and the body of checklist. A body of checklist can
contain the next commands.
* `\QRHitem`: an item of a checklist, 2 parameters: checklist item, and checklist action, like "Engine 1 Fire Handle" "Pull".
* `\QRHitemcond`: a conditional item, 2 parameters: conditional sentence, and subitems:
  * `\QRHsubitem`: like \itemcl. Currently is not possible to have `\itemcond` nested.
* `\QRHpart`: creates a new set of checklists. One parameter: part name like "NORM CHECKLIST".
* `\QRHspace`: a space between two items.
* `\QRHblank`: it prints at center of a page 'intentionally left blank'. Note: you need to put `\newpage` in any case.

Also there is `\QRHsymalert` that insert a banner in the bottom of the page to alert do not use this checklist for real aviation. You have to put `\QRHsymalert` just before`\newpage`.


