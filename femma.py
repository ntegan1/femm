import femm
#-- 0mag,1ele,2hea,3curr
femm.openfemm()
magneticsproblem = 0
femm.newdocument(magneticsproblem)
#femm.showconsole()
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

labelax = rectax1 + rectalen / 2.0
labelay = rectay1 + rectalen / 2.0
labelbx = rectbx1 + rectblen / 2.0 # TODO
labelby = rectby1 + rectblen / 2.0 # TODO
femm.mi_addblocklabel(
  labelax,
  labelay
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

airblock='Air'
polepieceblock='416 Stainless Steel'
steelblock='1006 Steel'
magnetblock='NdFeB 37 MGOe'
femm.mi_seteditmode('blocks')
femm.mi_getmaterial(
  steelblock
)
femm.mi_selectlabel(
  labelax,
  labelay
)
femm.mi_setblockprop(
  steelblock,
  1, # automesh
  0, # meshsizeconstraint
  None, # in circuit
  0, #None, # magnetization angle
  0, # group number
  0, # num turns
)
#femm.mi_setgroup(n) # set group of selected item to n
femm.mi_getmaterial(
  magnetblock
)
femm.mi_selectlabel(
  labelbx,
  labelby
)
femm.mi_setblockprop(
  magnetblock,
  1, # automesh
  0, # meshsizeconstraint
  None, # in circuit
  90, #None, # magnetization angle
  0, # group number
  0, # num turns
)
import time
time.sleep(100)
