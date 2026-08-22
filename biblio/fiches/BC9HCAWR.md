# [A design of interactive review for computer aided diagnosis of pulmonary nodules based on active learning].

**Auteurs** : Shuangping Tan, Jun Li, Xiaojuan Zhang, Xinyue Yan, Tong Zhang, Xiali Wu, Ziqiang Liu, Lili Li, Juan Feng, Haibin Han, Guoying Tang, Junzhou Han, Youfeng Deng
**Année** : 2024
**DOI** : 10.7507/1001-5515.202310044

## Résumé

Automatic detection of pulmonary nodule based on computer tomography (CT) images can significantly improve the diagnosis and treatment of lung cancer. However, there is a lack of effective interactive tools to record the marked results of radiologists in real time and feed them back to the algorithm model for iterative optimization. This paper designed and developed an online interactive review system supporting the assisted diagnosis of lung nodules in CT images. Lung nodules were detected by the preset model and presented to doctors, who marked or corrected the lung nodules detected by the system with their professional knowledge, and then iteratively optimized the AI model with active learning strategy according to the marked results of radiologists to continuously improve the accuracy of the model. The subset 5-9 dataset of the lung nodule analysis 2016(LUNA16) was used for iteration experiments. The precision, F1-score and MioU indexes were steadily improved with the increase of t

## Méthodologie

{'study_design': "设计并开发一个在线交互审查系统，包括肺结节分割模型、主动学习中间件和医生审查纠错3个模块，采用'交互标记-标签传播-样本集扩展-分割模型更新'的技术路线，通过多轮迭代实验验证模型性能提升", 'intervention': '系统使用3D-UNet模型进行肺结节检测，医生通过交互界面对检测结果进行标注或纠正，基于3D-HOG特征相似的标签传播策略扩展主动学习候选样本集，并采用融合Dice损失和交叉熵损失（含对数惩罚项）的加权损失函数对模型进行增量式重训练', 'control': None, 'primary_outcomes': ['Precision（精确率）', 'F1 score', 'MioU（平均交并比）'], 'secondary_outcomes': [], 'statistical_methods': ['戴斯系数(Dice)计算', '加权Dice损失函数', '交叉熵损失及对数惩罚项', '3D方向梯度直方图(3D-HOG)特征相似度计算'], 'duration': None, 'setting': '基于LUNA16数据集子集5-9的迭代实验'}

## Résultats

{'quantitative': [{'outcome': 'Precision', 'value': '从0.2139提高到0.5656', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'The precision, F1score and MioU indexes were steadily improved with the increase of the number of iterations, and the precision increased from 0.213 9 to 0.565 6.'}, {'outcome': 'F1 score', 'value': '随迭代次数增加稳步提升（具体数值未在提供文本中给出）', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'The precision, F1score and MioU indexes were steadily improved with the increase of the number of iterations'}, {'outcome': 'MioU', 'value': '随迭代次数增加稳步提升（具体数值未在提供文本中给出）', 'unit': None, 'confidence_interval': None, 'p_value': None, 'effect_size': None, 'source_section': 'Abstract', 'source_quote': 'The precision, F1score and MioU indexes were steadily improved with the increase of the number of iterations'}], 'qualitative_findings': [], 'main_findings': ['该系统能在使用深度分割模型辅助医生诊断的同时，最大程度地利用医生的反馈信息来优化模型', '随着迭代次数的增加，Precision、F1 score和MioU指标稳步提升', '系统将肺结节检测、医生审查标注、模型优化等功能集于一体']}

## Conclusions

该系统不仅使用深度分割模型辅助放射科医生，还最大程度地利用放射科医生的反馈信息优化模型，迭代提高模型的准确性，从而更好地辅助放射科医生工作 本文设计的损失函数和主动学习优化方法可作为其他肺结节分割模型及系统设计的有效参考

### Formule


$$0 引言 肺癌是一种临床常见的恶性肿瘤，在全球范围 内都具有较高发病率和死亡率 [1] 。若能在早期进行 检测并治疗，患者的五年存活率将得到大幅提高 [2] 。 早期肺癌在计算机断层扫描(computed tomo- graphy，CT)图像中表现为肺结节，呈圆形不透明 或不规则阴影。随着医学成像技术的迅猛发展， CT图像分辨率不断提高，能够捕捉到更小尺寸的 肺部病灶，这为肺结节的精准诊断提供了可能。 在庞大的CT图像中判读各类复杂肺结节，且 保持较高的准确率和效率，对临床医生来说是一个 较大挑战。计算机辅助诊断(computer aided diagnosis，CAD)通过人工智能(artificial intel- ligence，AI)算法实现诊断过程的自动化，可有效提 高诊断结果的准确率和放射科医生的工作效率 [3] 。 近年来，随着深度学习的应用，针对CT影像的 CAD进展迅速，涵盖了数据预处理、肺实质分割、 肺结节检测、假阳性降低、肺结节分割、分类和检$$

### Formule


$$现，现阶段CT图像肺结节分割存在两个问题： ① 肺结节目标小，且具有准确像素级结节标签的 数据集获取困难，常见的通用深度分割模型表现欠 佳；② 不能有效地集成医生的反馈，无法充分利 用医生的专业知识。 针对上述问题，本文设计并研发了一个支持 CT图像肺结节辅助诊断的在线交互审查方法和系 统，提出"交互标记-标签传播-样本集扩展-分割模 型更新"的技术路线。其创新点包括：① 对肺结 节像素级标签难以获取问题，设计了基于三维方向 的梯度直方图(three dimensional histogram of oriented gradients，3D-HOG)提取特征相似的标签 传播策略，顾及不确定性和多样性，扩展用于主动 学习样本选择的候选样本集；② 提出了基于交互 图形界面的医生审查系统的设计与实现方法。 本文设计系统首先将检测出的肺结节展示给 医生，医生利用专业知识对系统检测出的肺结节进 行标注或纠正，然后根据标注结果采用标签传播的 主动学习策略对内置模型进行迭代优化，以持续提 高模型的准确性。本系统将肺结节检测、医生审查 标注、模型优化等功能集于一体，在使用AI模型辅 助医生诊断的同时，又最大程度利用医生的反馈信 息来优化模型。本文设计的损失函数和主动学习 优化方法，可作为任何一个肺结节分割模型及系统 设计的有效参考，以迭代提高模型的准确性，更好 地辅助医生工作。 1 基于主动学习的肺结节辅助诊断交互审 查系统设计 1.1 系统整体设计 本文介绍的肺结节CAD交互审查系统，是基 于主动学习驱动的诊断方法。主动学习是通过假 设样本池中每个样本对模型性能的提高贡献不 同，每次迭代训练时选取信息量最大、价值最高的$$

### Formule


$$系统首先通过内置模型检测出肺结节，提供图形 化界面让多位医生对模型的初步检测结果进行标 注或纠正，然后从训练数据集和待诊断数据集中 同时筛选信息量较高的样本对模型进行更新训练， 直至分割模型达到精度要求或不再提升。本文主 动学习中使用的选择策略是人工引导的样本选取 策略，其综合多位医生的投票得分和模型表现来 设定各样本的信息量，以提高分割模型在特定类 型结节的检测敏感度，改善肺结节多样性和类别 不平衡带来的假阳性问题。该方法在原有样本数 据基础上，每次逐渐增加主动学习样本(约占原样 本数据1/4到1/5)，以便在训练过程中保留对旧 数据的记忆，同时为了避免新数据对模型产生过 大影响，算法会适当降低学习率使模型对旧知识 的保留更稳定。 本文介绍的交互性包括两方面：① 用户可对 模型检测出的肺结节结果进行审查标注，并返回样 本，返回的样本通过主动学习持续改进后台模型。 ② 多用户可同步或异步进行审查标注，算法会利 用多用户交互标注信息进行用户不确定度计算，帮 助筛选更有价值的样本进行模型优化。 1.2 功能和流程设计 如图1所示，本系统主要包括肺结节分割模 型、主动学习中间件和医生审查纠错3个模块，分 别完成基于主动学习模型的肺结节分割、分割模型 重训练、基于网页浏览器(web browser，web)的原 始图像和检测结果可视化展示及用户交互。各模 块按顺序进行的主要功能如下： (1)肺结节分割：对用户传入的原始CT图像 进行肺结节检测，并将分割结果同时传输给前端可 视化界面和中间件样本选择算法。 (2)分割结果处理与展示：后端通过连通域计 算，获得已分割的肺结节实例列表，并与原始CT 图像一起呈现给用户。 (3)医生审查：结合原始CT图像，多位医生 通过交互界面对分割出的肺结节进行审查，对漏检 或错检的肺结节切片以画圈的方式进行粗糙标记 和纠正。 (4)基于主动学习的样本筛选：当新增或修改 的肺结节标记达到一定数量时，后端将医生的审查 标注结果和原始分割结果一同传输给在线样本选 择模型，应用于三维U型网络(3D-Unet)模型的更 新训练。 (5)模型重训练与更新：在构建的训练集基础 上，以增量方式优化当前模型。 (6)循环执行步骤(1)～步骤(5)，直至分割模 型达到精度要求或不再提升，在此过程中用户可持 续输入未诊断的CT图像。通过不断迭代，使后台 分割模型不断收到医生的反馈，从而有效地融合医 生专业知识，提高模型的泛化能力和分割性能。 1.2.1 肺结节分割模型 3D-UNet模型是一种经典 的卷积神经网络结构，能够同时捕获图像中的局部 细节和全局上下文信息，因此常用于医学影像分割$$

### Formule


$$合了医学图像分割常用的戴斯(Dice)损失和交叉 熵损失来设计损失函数。考虑到医生提供的标注 数量有限，在模型重训练过程中，对医生未标记的 区域进行相对粗糙的样本扩展。然后根据3D-HOG 提取纹理特征向量，计算未标记样本和具有精细标 签的本地训练集的相似性来获取未标记样本的伪 标签，并将相似距离加入到加权Dice 损失函数的 设计中 [19] ，如式(1)所示： dice = 1-(αD p + (1-α)D n ) (1) 其中，D p 和D n 分别表示肺结节像素和背景像 素的戴斯系数(以符号dice表示)，超参数α由最 小传播距离计算，具体细节如式(2)～式(4)所示： D p = 2|X p ∩ Y p | |X p | + |Y p | (2) D n = 2|X n ∩ Y n | |X n | + |Y n | (3) α =$$

### Formule


$$X p 、X n 、Y p 、Y n 分别表示实际标注为结节、预测 结果为结节、实际标注为背景、预测结果为背景的 概率矩阵。r neg 和r pos 分别表示根据最小相似距离 计算的背景和结节像素数所占的比值，其计算公式 如式(5)～式(8)所示： r neg = p neg p pos + p neg(5)$$

### Formule


$$p neg = ∑ 1 min distance + 1$$

### Formule


$$p pos = ∑ 1 min distance + 1 • n pos (8) 其中，min distance 为最小相似距离，n neg 和 n pos 分别表示标签传播后具有粗糙标签的切块中结 节和背景的像素数，p neg 和p pos 分别表示标签传播 后根据最小相似距离加权得到的背景和结节像 素数。 此外，基于交叉熵损失函数的梯度稳定性，添 加了结节和背景像素的对数惩罚项pen p 和pen n ， 如式($$

### Formule


$$pen p =- ∑ i∈P log(y i + ε) (9$$

### Formule


$$)$$

### Formule


$$pen n =- ∑ i∈N log[(1-y i ) + ε] (10) 其中，y i 表示预测结果像素为肺结节的概率， ε为一个极小值，防止对数的真数为0造成错误。 通过多次实验验证，设置超参数ω = 2，λ = 0.2，最 终损失函数(以符号loss表示)如式(11)$$
