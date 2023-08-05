import femm
#-- 0mag,1ele,2hea,3curr
femm.openfemm()
magneticsproblem = 0
femm.newdocument(magneticsproblem)
femm.showconsole()
#femm.clearconsole()

rectax1 = 0.5
rectay1 = 0.5
rectax2 = 1.0
rectay2 = 1.0
rectbx1 = 0.1
rectby1 = 0.1
rectbx2 = 0.33
rectby2 = 0.33
rectalen = rectax2 - rectax1 #-- square
rectblen = rectbx2 - rectbx1 #-- square
femm.mi_drawrectangle(
  rectax1,
  rectay1,
  rectax2,
  rectay2,
)
femm.mi_drawrectangle(
  rectbx1,
  rectby1,
  rectbx2,
  rectby2,
)
#femm.hidepointprops()

femm.mi_addblocklabel(
  rectax1 + rectalen / 2.0,
  rectay1 + rectalen / 2.0
)
femm.mi_addblocklabel(
  rectbx1 + rectblen / 2.0,
  rectby1 + rectblen / 2.0
)

# x axis
femm.mi_drawline(
  -1.0, 0.0, 1.0, 0.0
)
# y axis
femm.mi_drawline(
  0, -1., 0, 1.
)

import time
time.sleep(10)
