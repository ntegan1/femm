import femm
#-- 0mag,1ele,2hea,3curr
femm.openfemm()
magneticsproblem = 0
img_num=0
femm.newdocument(magneticsproblem)
#femm.showconsole()
#femm.clearconsole()
# .13 and .8

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
labelairx = 0
labelairy = 1.5
femm.mi_addblocklabel(
  labelax,
  labelay
)
femm.mi_addblocklabel(
  labelairx,
  labelairy
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
# 7 layer 2.14 radius dirichlet iabc
# for anti periodic set bdryformat 5, all other params 0
#femm.mi_addboundprop('propname', 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0)
#femm.mi_addboundprop(0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0)
femm.mi_makeABC(
  #n, R, x, y, bc
  7, 2.12132, 0, 0, 0
)
femm.mi_clearselected()
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
femm.mi_clearselected()
femm.mi_getmaterial(
  airblock
)
femm.mi_selectlabel(
  labelairx,
  labelairy
)
femm.mi_setblockprop(
  airblock,
  1, # automesh
  0, # meshsizeconstraint
  None, # in circuit
  0, #None, # magnetization angle
  0, # group number
  0, # num turns
)
femm.mi_saveas('b.FEM')
femm.mi_analyze(0) # visible 0
# current density props
#0.000948046692546575
#0.72
femm.mi_loadsolution()
#femm.mo_showdensityplot(
#  1, 0, 2.0, 0.05, 'bmag'
#)
femm.mo_showdensityplot(
  1, 0, .8, .13, 'bmag'
)
# TODO
# zoom in proper
#-.25, .64 tl
# .82, 0. br
# api is bl to tr
# NEED TO FIX
femm.mi_zoom(
  -.25, 0., .82. .64
)

img_num=4
file = "img/" + str(img_num) + ".bmp"
femm.mo_savebitmap(
  file
)

import time
time.sleep(100000)
