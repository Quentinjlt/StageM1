from py_post import *
from py_mentat import *
import numpy as np
def main():
    print("DEBUT")
    p = post_open("modeleassembly_modeleassembly_groupe_80um_axex.t16")
    filetemperature_nameface=open("Temperature_nameface.txt",'w')
    filetemperature_namenode=open("Temperature_namenode.txt",'w')
    filevector_namenode=open("Flux_namenode.txt",'w')
    filevector_nameface=open("Flux_nameface.txt",'w')
    filemoy=open("Moyenne_temperature&flux_conductivite.txt",'w')
    p.moveto(2)
    name_node="Element_noeud"
    name_face="Element_face"
    nb_set_now=py_get_int("nsets()")
    for set_now in range(1,nb_set_now+1):
        id_set_now=py_get_int("set_id(%d)"%(set_now))
        set_name_now=py_get_string("set_name(%d)"%(id_set_now))
        if set_name_now==name_node:
            set_entries_now_namenode=py_get_int("nset_entries(%d)"%(id_set_now))
            nsc_namenode = p.node_scalars()
            nesc_namenode = p.element_scalars()
            check_namenode=0
            moyenne_temperature_namenode=0
            moyenne_heat_flux_namenode=0
            nb_element_analyse_namenode=0
            for element_namenode in range (1,(set_entries_now_namenode+1)):
                id_element_namenode=py_get_int("set_entry(%d,%d)"%(id_set_now,element_namenode))
                element_node_namenode=py_get_int("element_nodes(%d)"%id_element_namenode)
                moyenne_temperature_element_bynode_namenode=[]
                tri_namenode=0
                for node_namenode in range(1,(element_node_namenode+1)):
                    id_loc_node_element_namenode=py_get_int("element_node_id(%d,%d)"%(id_element_namenode,node_namenode))
                    coord_x_namenode=round(py_get_float("node_x(%d)"%(id_loc_node_element_namenode)),5)
                    coord_y_namenode=round(py_get_float("node_y(%d)"%(id_loc_node_element_namenode)),5)
                    coord_z_namenode=round(py_get_float("node_z(%d)"%(id_loc_node_element_namenode)),5)
                    for node_temp_namenode in range(0,nsc_namenode):
                        label1_namenode=p.node_scalar_label(node_temp_namenode)
                        if label1_namenode=="Temperature":
                            if coord_x_namenode==0.12600:
                                temp_namenode=p.node_scalar((id_loc_node_element_namenode-1),node_temp_namenode)
                                if temp_namenode != 0
                                    filetemperature_namenode.write("ID Element : %d, ID Node : %s, temperature = %d,x=%f / y=%f / z=%f\n"%(id_element_namenode,id_loc_node_element_namenode,temp_namenode,coord_x_namenode,coord_y_namenode,coord_z_namenode))
                                    moyenne_temperature_element_bynode_namenode.append(temp_namenode)
                    if coord_x_namenode==0.12600:
                        tri_namenode=tri_namenode+1
                        if tri_namenode==4:
                            for element_scalar_namenode in range (0,nesc_namenode):
                                label_element_namenode=p.element_scalar_label(element_scalar_namenode)
                                if (label_element_namenode == "1st Comp of Heat Flux"):
                                    heat_flux_namenode=p.element_scalar((id_element_namenode-1),element_scalar_namenode)
                                    len_heat_flux_namenode=len(heat_flux_namenode)
                                    k_namenode=0
                                    while k_namenode < len_heat_flux_namenode :
                                        value_heat_flux_namenode=heat_flux_namenode[k_namenode].value
                                        k_namenode=k_namenode+1
                                    moyenne_heat_flux_namenode=moyenne_heat_flux_namenode+value_heat_flux_namenode
                                    nb_element_analyse_namenode=nb_element_analyse_namenode+1
                                    filevector_namenode.write("ID Element : %d, Nb Analysé : %d, Vecteur : %s\n"%((id_element_namenode-1),nb_element_analyse_namenode,value_heat_flux_namenode))
                                    tri_namenode=0
                check_namenode=check_namenode+1
                nb_noeud_temp_byelement_namenode=len(moyenne_temperature_element_bynode_namenode)
                moyenne_temperature_element_namenode=sum(moyenne_temperature_element_bynode_namenode)/(nb_noeud_temp_byelement_namenode)
                moyenne_temperature_namenode=moyenne_temperature_namenode+moyenne_temperature_element_namenode
        if set_name_now==name_face:
            set_entries_now_nameface=py_get_int("nset_entries(%d)"%(id_set_now))
            nsc_nameface = p.node_scalars()
            nesc_nameface = p.element_scalars()
            check_nameface=0
            moyenne_temperature_nameface=0
            moyenne_heat_flux_nameface=0
            nb_element_analyse_nameface=0
            for element_nameface in range (1,set_entries_now_nameface+1):
                id_element_nameface=py_get_int("set_entry(%d,%d)"%(id_set_now,element_nameface))
                element_node_nameface=py_get_int("element_nodes(%d)"%id_element_nameface)
                moyenne_temperature_element_bynode_nameface=[]
                tri_nameface=0
                for node_nameface in range(1,(element_node_nameface+1)):
                    id_loc_node_element_nameface=py_get_int("element_node_id(%d,%d)"%(id_element_nameface,node_nameface))
                    coord_x_nameface=round(py_get_float("node_x(%d)"%(id_loc_node_element_nameface)),5)
                    coord_y_nameface=round(py_get_float("node_y(%d)"%(id_loc_node_element_nameface)),5)
                    coord_z_nameface=round(py_get_float("node_z(%d)"%(id_loc_node_element_nameface)),5)
                    for node_temp_nameface in range(0,nsc_nameface):
                        label1_nameface=p.node_scalar_label(node_temp_nameface)
                        if label1_nameface=="Temperature":
                            if coord_x_nameface==0.13592:
                                temp_nameface=p.node_scalar((id_loc_node_element_nameface-1),node_temp_nameface)
                                if temp_nameface != 0:
                                    filetemperature_nameface.write("ID Element : %d, ID Node : %s, temperature = %d,x=%d / y=%d / z=%d\n"%(id_element_nameface,id_loc_node_element_nameface,temp_nameface,coord_x_nameface,coord_y_nameface,coord_z_nameface))
                                    moyenne_temperature_element_bynode_nameface.append(temp_nameface)
                    if coord_x_nameface==0.13592:
                        tri_nameface=tri_nameface+1
                        if tri_nameface==4:
                            for element_scalar_nameface in range (0,nesc_nameface):
                                label_element_nameface=p.element_scalar_label(element_scalar_nameface)
                                if (label_element_nameface == "1st Comp of Heat Flux"):
                                    heat_flux_nameface=p.element_scalar((id_element_nameface-1),element_scalar_nameface)
                                    len_heat_flux_nameface=len(heat_flux_nameface)
                                    k_nameface=0
                                    while k_nameface < len_heat_flux_nameface :
                                        value_heat_flux_nameface=heat_flux_nameface[k_nameface].value
                                        k_nameface=k_nameface+1
                                    moyenne_heat_flux_nameface=moyenne_heat_flux_nameface+value_heat_flux_nameface
                                    nb_element_analyse_nameface=nb_element_analyse_nameface+1
                                    filevector_nameface.write("ID Element : %d, Nb Analysé : %d, Vecteur : %s\n"%((id_element_nameface-1),nb_element_analyse_nameface,value_heat_flux_nameface))
                                    tri=0
                check_nameface=check_nameface+1
                nb_noeud_temp_byelement_nameface=len(moyenne_temperature_element_bynode_nameface)
                moyenne_temperature_element_nameface=sum(moyenne_temperature_element_bynode_nameface)/(nb_noeud_temp_byelement_nameface)
                moyenne_temperature_nameface=moyenne_temperature_nameface+moyenne_temperature_element_nameface
    somme_heat_flux_namenode=pow(pow(moyenne_heat_flux_namenode,2),0.5)
    somme_heat_flux_nameface=pow(pow(moyenne_heat_flux_nameface,2),0.5)
    average_temp_namenode=(moyenne_temperature_namenode)/(check_namenode)
    average_temp_nameface=(moyenne_temperature_nameface)/(check_nameface)
    conductivite=(somme_heat_flux_namenode*0.00992/15376)/(average_temp_nameface-average_temp_namenode)
    filemoy.write("Temperature_namenode = %d\n"%(average_temp_namenode))
    filemoy.write("Temperature_nameface = %d\n"%(average_temp_nameface))
    filemoy.write("Flux moyen _namenode = %d\n"%(somme_heat_flux_namenode))
    filemoy.write("Flux moyen _nameface = %d\n"%(somme_heat_flux_nameface))
    filemoy.write("conductivité = %f\n"%(conductivite))
    filemoy.close()
    filevector_namenode.close()
    filevector_nameface.close()
    filetemperature_nameface.close()
    filetemperature_namenode.close()
    print("FIN")
if __name__ == '__main__':
    main();
