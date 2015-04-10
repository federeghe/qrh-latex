# qrh-latex
Quick Reference Handbook package for LaTeX.

Quick Reference Handbooks or QRHs are specific manuals used by pilots. A QRH contains all normal and abnormal procedures for flying a specific
aircraft. A more detailed definition can be found [at skybrary](http://www.skybrary.aero/index.php/Quick_Reference_Handbook).

Exposed commands
----------------

You should separate each page with `\newpage` and set as first the `\headingcl` (explained below). You should not split the checklist in more pages.

This package contains few commands easy to use:
* `\headingcl`: it is the header of each page. It has 4 parameters: aircraft short name (A320, B737, P180, etc.), checklist group name (NORMAL
CHECKLIST, ABNORMAL PROCEDURES, etc.), revision number, and the section number.
* `\bodycl`: it is the body of each checklist. If checklists are short you can put them in the same page, but remember: never split a checklist over
two pages! (Also this is never done in real aviation QRH). It accepts 2 parameters: checklist name, and the body of checklist. A body of checklist can
contain the next commands.
* `\itemcl`: an item of a checklist, 2 parameters: checklist item, and checklist action, like "Engine 1 Fire Handle" "Pull".
* `\itemcond`: a conditional item, 2 parameters: conditional sentence, and subitems:
  * `\subitemcl`: like \itemcl. Currently is not possible to have `\itemcond` nested.
* `\spacecl`: a space between two items.

Also there is `\symalert` that insert a banner in the bottom of the page to alert do not use this checklist for real aviation. You have to put `\symalert` just before`\newpage`.


