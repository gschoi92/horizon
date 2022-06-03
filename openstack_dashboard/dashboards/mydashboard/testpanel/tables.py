from tabnanny import verbose
from django.utils.translation import gettext_lazy as _
from horizon import tables

class InstanceTable(tables.DataTable):
    projectName = tables.Column("projectName", verbose_name=_("Project name")) 
    type = tables.Column("type", verbose_name=_("Product type"))
    resourceName = tables.Column("resourceName", verbose_name=_("Resource name"))
    contractId = tables.Column("contactId", verbose_name=_("Contract ID"))
    chargeName = tables.Column("chargeName", verbose_name=_("Charge Name"))
    bill = tables.Column("bill", verbose_name=_("Bill Amount"),)
    billStatus = tables.Column("billStatus", verbose_name=_("Bill Status"), 
                               status_choices=(
                                   ('yes',True),
                                   ('no', False),
                                   ))
    date = tables.Column("date", verbose_name=_("Date"))
    
    class Meta(object):
        name = "monthly"
        verbose_name=_("Payment monthly")
        