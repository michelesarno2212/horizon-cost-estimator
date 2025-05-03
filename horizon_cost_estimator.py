{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import openstack\
\
def calculate_volume_cost():\
    conn = openstack.connect()\
    volumes = conn.block_storage.volumes()\
\
    total_size_gb = 0\
    num_volumes = 0\
\
    for vol in volumes:\
        total_size_gb += vol.size\
        num_volumes += 1\
\
    cost_per_gb = 0.05  # default costo per GB\
    cost_per_volume = 2.0  # default costo per volume\
\
    total_cost = (total_size_gb * cost_per_gb) + (num_volumes * cost_per_volume)\
    return \{\
        "total_size_gb": total_size_gb,\
        "num_volumes": num_volumes,\
        "estimated_cost": total_cost\
    \}\
\
if __name__ == "__main__":\
    result = calculate_volume_cost()\
    print(f"Total Size (GB): \{result['total_size_gb']\}")\
    print(f"Number of Volumes: \{result['num_volumes']\}")\
    print(f"Estimated Cost: $\{result['estimated_cost']:.2f\}")\
}