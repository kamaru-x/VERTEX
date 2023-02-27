from administrator.models import User,Sales_Target,Proposal
from datetime import date

def setTarget():
    salesmans = User.objects.filter(is_salesman=True)
    d = date.today()
    year = d.year
    for salesman in salesmans:
        archived = 0
        faild = 0
        pending = 0

        r_proposals = Proposal.objects.filter(Lead__Salesman=salesman,Proposal_Status=0,Date__year=year)
        a_proposals = Proposal.objects.filter(Lead__Salesman=salesman,Proposal_Status=1,Date__year=year)
        p_proposals = Proposal.objects.filter(Lead__Salesman=salesman,Proposal_Status=10,Date__year=year)

        for a in a_proposals:
            if a.Grand_Total:
                archived += int(a.PO_Value)

        for r in r_proposals:
            if r.Grand_Total:
                faild += r.Grand_Total

        for p in p_proposals:
            if p.Grand_Total:
                pending += p.Grand_Total

        target = Sales_Target.objects.filter(Salesman=salesman,From__year=year).last()
        if target:
            target.Archived = archived
            target.Failed = faild
            target.Pending = pending
            target.Balance = target.Targets - archived
            target.save()