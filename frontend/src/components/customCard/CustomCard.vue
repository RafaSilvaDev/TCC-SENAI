<template> 
    <div class="card-all">
        <div class="custom-card">
            <div class="content-card">
                <div>
                    <div class="card-header">
                        <div class="header__left">
                            <span>#{{id}}</span>
                        </div>
                        <div class="header__right">
                            <Icon v-if="type!='pdf'" iconName="refresh" className="a-button__icon" @click="front = !front"/>
                            <Icon iconName="fullscreen" className="a-button__icon" @click="showPopUp = true"/>
                            <div v-if="dateRead!=='no'" :class="['dot-status', [dateRead ? '-on' : '-off' ]]" :data-text="'Lido em '+ dateRead"></div>
                        </div>
                    </div>
                    <div class="card-body">
                        <div :class="['content-body__front', [{'-face': front}]]">
                            <div class="text">
                                <h5 class="title">{{title}}</h5>
                                <p>Lorem ipsum consectetur adipiscing elit. Phasellus eu dictum diam, eu hendrerit est. Etiam venenatis hendrerit nunc, eget accumsan libero congue quis. Nulla facilisi. Maecenas nec tellus tellus. Donec luctus in lacus ut vehicula. Quisque aliquam hendrerit condimentum. Aliquam placerat risus ipsum, vitae porttitor turpis ornare id. Sed arcu lectus, iaculis at purus id, posuere varius eros.</p>
                            </div>
                            <!-- <img v-if="data.img" :src="data.img" alt=""> -->
                        </div>
                        <div v-if="type!='pdf'" :class="['content-body__back', [{'-face': !front}]]">
                            <div class="text">
                                <h5 class="title">BACK</h5>
                                <p>Etiam venenatis hendrerit nunc, eget accumsan libero congue quis. Nulla facilisi.Quisque aliquam hendrerit condimentum. Sed arcu lectus, iaculis at purus id, posuere varius eros.</p>
                            </div>
                            <!-- <img v-if="data.img" :src="data.img" alt=""> -->
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <Box v-if="havePopUp" :show="showPopUp">
            <div v-if="type!='pdf'" class="custom-card -popUp">
                <div class="content-card">
                    <div>
                        <div class="card-header">
                            <div class="header__left">
                                <span>#{{id}}</span>
                            </div>
                            <div class="header__right">
                                <Icon iconName="refresh" className="a-button__icon" @click="frontPopUp = !frontPopUp"/>
                                <Icon iconName="close" className="a-button__icon" @click="showPopUp = false"/>
                                <div v-if="dateRead!=='no'" :class="['dot-status', [dateRead ? '-on' : '-off' ]]" :data-text="'Lido em '+ dateRead"></div>
                            </div>
                        </div>
                        <div class="card-body">
                            <div :class="['content-body__front', [{'-face': frontPopUp}]]">
                                <div class="text">
                                    <h5 class="title">{{title}}</h5>
                                    <p>Lorem ipsum consectetur adipiscing elit. Phasellus eu dictum diam, eu hendrerit est. Etiam venenatis hendrerit nunc, eget accumsan libero congue quis. Nulla facilisi. Maecenas nec tellus tellus. Donec luctus in lacus ut vehicula. Quisque aliquam hendrerit condimentum. Aliquam placerat risus ipsum, vitae porttitor turpis ornare id. Sed arcu lectus, iaculis at purus id, posuere varius eros.</p>
                                </div>

                            </div>
                            <div :class="['content-body__back', [{'-face': !frontPopUp}]]">
                                <div class="text">
                                    <h5 class="title">BACK</h5>
                                    <p>Etiam venenatis hendrerit nunc, eget accumsan libero congue quis. Nulla facilisi.Quisque aliquam hendrerit condimentum. Sed arcu lectus, iaculis at purus id, posuere varius eros.</p>
                                </div>

                            </div>       
                        </div>
                    </div>
                </div>
            </div>
            <div v-else class="pdf-viewer">
                <Icon iconName="close" className="a-button__icon" @click="showPopUp = false"/>
                <embed v-if="showPopUp" :src="urlPdf.concat('#toolbar=0&scrollbars=0&navpanes=0&zoom=150&scrollbar=0')" type="application/pdf">
            </div>
        </Box>
    </div>
</template>

<script>
import Icon from '@/components/icon/Icon.vue';
import Box from '@/components/box/Box.vue';

export default {
    data: function() {
        return {
            front: true,
            frontPopUp: true,
            showPopUp: false,
            urlPdf: 'http://www.defensoria.pi.gov.br/gestor/public/uploader/documentos/4/84a0bcaa34768dfdbc090b3caab1b660.pdf'
        }
    },
    props: [ 'id', 'title', 'textFront', 'textBack', 'img', 'dateRead', 'havePopUp', 'type' ],
    components: {
        Icon,
        Box,
    },
}
</script>

<style src="./customCard.scss" lang="scss"></style>